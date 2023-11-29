import { createQueue } from 'kue';

const messageQueue = createQueue();

const jobObject = {
  phoneNumber: '+246-89687697',
  message: 'This a dummy message'
};

const queueName = 'push_notification_code';

const job = messageQueue.create(queueName, jobObject).save();
job.on('enqueue', (createdJob) => {
  console.log(`Notification job created: ${job.id}`);
});

job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', () => {
  console.log('Notification job failed');
});
