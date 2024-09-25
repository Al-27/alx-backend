import redis from 'redis';

const clnt = redis.createClient();

clnt.on('connect', () => {
  console.log('Redis client connected to the server');
});

clnt.on('error', (e) => {
  console.error(`Redis client not connected to the server: ${e}`);
});

async function create_hash(id, key, val) {
        await clnt.hset(id, key, val,redis.print);
}

create_hash("HolbertonSchools", "Portland", '50');
create_hash("HolbertonSchools", "Seattle", '80');
create_hash("HolbertonSchools", "New York", '20');
create_hash("HolbertonSchools", "Bogota", '20');
create_hash("HolbertonSchools", "Cali", '40');
create_hash("HolbertonSchools", "Paris", '2');

clnt.hgetall("HolbertonSchools", (er,res)=>{
    if (er) {
        return;
    }
    else
        console.log(res);
});
