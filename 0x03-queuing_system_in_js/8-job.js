function createPushNotificationsJobs (jobs, queue) {
  const queueName = 'push_notification_code_3';
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }
  jobs.forEach((job) => {
    const newJob = queue.create(queueName, job).save();
    newJob.on('enqueue', () => console.log(`Notification job created: ${newJob.id}`));
    newJob.on('complete', () => console.log(`Notification job ${newJob.id} completed`));
    newJob.on('failed', (err) => console.log(`Notification job ${newJob.id} failed: ${err}`));
    newJob.on('progress', (progress) => console.log(`Notification job ${newJob.id} ${progress}% complete`));
  });
}

module.exports = createPushNotificationsJobs;
