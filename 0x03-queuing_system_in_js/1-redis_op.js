import redis from 'redis';

const client = redis.createClient({
  host: 'localhost', // Replace with your Redis server host
  port: 6379, // Replace with your Redis server port
});

client.on('connect', function () {
  console.log('Redis client connected to the server');
});

client.on('error', function (err) {
  console.error('Redis client not connected to the server: ' + err.message);
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

function displaySchoolValue(schoolName) {
  client.get(schoolName, function(err, reply) {
    if (err) throw err;
    console.log(reply);
  });
}

displaySchoolValue('ALX');
setNewSchool('ALXSanFrancisco', '100');
displaySchoolValue('ALXSanFrancisco');
