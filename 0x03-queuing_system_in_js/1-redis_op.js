import redis from 'redis';

const clnt = redis.createClient();

clnt.on('connect', () => {
  console.log('Redis client connected to the server');
});

clnt.on('error', (e) => {
  console.error(`Redis client not connected to the server: ${e}`);
});

function setNewSchool(schName, val) {
    clnt.set(schName, val, redis.print);
}

function displaySchoolValue(schName) {
    clnt.get(schName, (e,res) => {
    console.log(res);
  });
}


displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
