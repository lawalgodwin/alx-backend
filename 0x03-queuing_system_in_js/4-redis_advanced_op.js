import redis  from 'redis'
import redisClient from './0-redis_client'

const hKey = 'HolbertonSchools'

redisClient.hset(hKey, 'Portland', '50', redis.print)
redisClient.hset(hKey, 'Seattle', '80', redis.print)
redisClient.hset(hKey, 'New York', '20', redis.print)
redisClient.hset(hKey, 'Bogota', '20', redis.print)
redisClient.hset(hKey, 'Cali', '40', redis.print)
redisClient.hset(hKey, 'Paris', '2', redis.print)

redisClient.hgetall(hKey, (err, data) => {
    if (err) throw Error(err.message)
    console.log(data)
})
