import { createQueue } from 'kue';

const queue = createQueue();

const sendNotification = (phoneNumber, message) => {
  console.log(` Sending notification to ${phoneNumber}, with message: ${message}`);
};

const queueName = 'push_notification_code';

queue.process(queueName, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message);
  done();
});
