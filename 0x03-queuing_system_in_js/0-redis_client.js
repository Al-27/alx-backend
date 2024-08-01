import redis from 'redis';

const clnt = redis.createClient();

clnt.on('connect', () => {
  console.log('Redis client connected to the server');
});

clnt.on('error', (e) => {
  console.error(`Redis client not connected to the server: ${e}`);
});