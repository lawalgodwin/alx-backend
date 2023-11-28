import redisClient from './0-redis_client';
import redis from 'redis'

const setNewSchool = (schoolName, value) => {
    redisClient.set(schoolName, value, redis.print);
    // redisClient.set(schoolName, value, (err, reply) => redis.print(err, reply));
}

const displaySchoolValue = (schoolName) => {
    redisClient.get(schoolName, (err, result) => {
        if (err) throw Error(err.message)
        console.log(result)
    });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
