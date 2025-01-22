const { Worker } = require('worker_threads');

// Shared data structure for communication
const sharedData = {
  queue: [],
  limit: 5,
};

// Create a producer worker
const producerWorker = new Worker('./producer.js', {
  workerData: sharedData,
});

// Create a consumer worker
const consumerWorker = new Worker('./consumer.js', {
  workerData: sharedData,
});

// Listen for messages from the producer and consumer
producerWorker.on('message', (message) => {
  console.log(`Producer says: ${message}`);
});

consumerWorker.on('message', (message) => {
  console.log(`Consumer says: ${message}`);
});

// Handle errors
producerWorker.on('error', (err) => {
  console.error('Producer error:', err);
});

consumerWorker.on('error', (err) => {
  console.error('Consumer error:', err);
});
