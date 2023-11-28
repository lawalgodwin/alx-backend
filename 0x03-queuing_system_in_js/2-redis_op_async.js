import redisClient from './0-redis_client';
import {promisify} from 'util'
import redis from 'redis';

redisClient.get = promisify(redisClient.get)


const setNewSchool = (schoolName, value) => {
  redisClient.set(schoolName, value, redis.print);
  // redisClient.set(schoolName, value, (err, reply) => redis.print(err, reply));
};

const displaySchoolValue = async (schoolName) => {
  try {
    const result = await redisClient.get(schoolName);
    console.log(result);
  } catch (error) {
    throw new Error(error);
  }
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
