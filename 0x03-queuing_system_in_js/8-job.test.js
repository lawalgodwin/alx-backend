import { createQueue } from 'kue';
import { expect } from 'chai';

import createPushNotificationsJobs from './8-job';

const queueName = 'push_notification_code_3';

const queue = createQueue();

describe('test for createPushNotificationsJobs fuction', function () {
  before(() => {
    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.clear();
  });

  after(() => {
    queue.testMode.exit();
  });

  it('Test job creation with expected value', () => {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 1234 to verify your account'
      }
    ];
    createPushNotificationsJobs(jobs, queue);
    createPushNotificationsJobs(jobs, queue);
    expect(queue.testMode.jobs[0].type).to.equal(queueName);
    expect(queue.testMode.jobs[1].type).to.equal(queueName);
    expect(queue.testMode.jobs.length).to.equal(4);
    expect(queue.testMode.jobs[0].data).to.deep.equal(jobs[0]);
    expect(queue.testMode.jobs[1].data).to.deep.equal(jobs[1]);
  });

  it('Test for unexpected input', () => {
    const jobs = {
      phoneNumber: '4153518781',
      message: 'This is the code 1234 to verify your account'
    };
    expect(() => createPushNotificationsJobs(jobs, queue)).to.throw(Error, 'Jobs is not an array');
  });
});
