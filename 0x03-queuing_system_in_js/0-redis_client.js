'use strict';

import { createClient } from 'redis';

const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', err => console.log('Redis Client Error', err));
