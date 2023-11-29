import { createQueue } from 'kue';

const queue = createQueue();
const queueName = 'push_notification_code_2';
const blacklist = ['4153518780', '4153518781'];

const sendNotification = (phoneNumber, message, job, done) => {
  const totalFrame = 100;
  let completedFrame = 0;
  job.progress(completedFrame, totalFrame);
  if (blacklist.includes(phoneNumber)) {
    done(new Error(`Phone number ${phoneNumber} is blacklisted`));
    return;
  }
  completedFrame = 50;
  job.progress(completedFrame, totalFrame);
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  done();
};

queue.process(queueName, 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});
