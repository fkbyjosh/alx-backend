import { createClient, print } from 'redis';

const redisClient = createClient();

redisClient.on('connect', function() {
  console.log('Redis client connected to the server');
});

redisClient.on('error', function(error) {
  console.log(`Redis client not connected to the server: ${error}`);
});

//set hash key-value in HolbertonSchools list
redisClient.hset('ALX', 'Portland', '50', print);
redisClient.hset('ALX', 'Seattle', '80', print);
redisClient.hset('ALX', 'New York', '20', print);
redisClient.hset('ALX', 'Bogota', '20', print);
redisClient.hset('ALX', 'Cali', '40', print);
redisClient.hset('ALX', 'Paris', '2', print);

// retrieve all elements stored in HolbertonSchools list
redisClient.hgetall('ALX', function (error, result) {
  if (error) {
    console.log(error);
    throw error;
  }
  console.log(result);
});
