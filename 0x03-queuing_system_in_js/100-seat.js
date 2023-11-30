import { createClient } from 'redis';
import { createQueue } from 'kue';
import { promisify } from 'util';
import express from 'express';

const redisClient = createClient();

redisClient.get = promisify(redisClient.get);

const reserveSeat = (number) => redisClient.set('available_seats', number);

const getCurrentAvailableSeats = async () => {
  const currentlyAvailableNumberOfSeats = await redisClient.get('available_seats');
  return currentlyAvailableNumberOfSeats;
};

let reservationEnabled = true;

const queue = createQueue();
const queueName = 'reserve_seat';

const app = express();

app.get('/available_seats', async (req, res) => {
  const numberOfAvailableSeats = await getCurrentAvailableSeats();
  res.status(200).json({ numberOfAvailableSeats });
});

app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) return res.json({ status: 'Reservation are blocked' });
  const jobObject = {};
  const newJob = queue.create(queueName, jobObject);
  newJob.save((err, success) => {
    if (!err) return res.status(200).json({ status: 'Reservation in process' });
    return res.json({ status: 'Reservation failed' });
  });
  newJob.on('complete', () => console.log(`Seat reservation job ${newJob.id} completed`));
  newJob.on('failed', (err) => console.log(`Seat reservation job JOB_ID failed: ${err.message}`));
});

app.get('/process', (req, res) => {
  // process the queue
  queue.process(queueName, async (job, done) => {
    let numberOfAvailableSeats = await getCurrentAvailableSeats();
    if (numberOfAvailableSeats === 0) reservationEnabled = false;
    // reserve the remaining number of seats
    numberOfAvailableSeats = Number(numberOfAvailableSeats) - 1;
    reserveSeat(numberOfAvailableSeats);
    if (numberOfAvailableSeats >= 0) return done();
    return done(Error('Not enough seats available'));
  });
  res.json({ status: 'Queue processing' });
});

app.listen(1245, () => console.log('Server running on port 1245'));
