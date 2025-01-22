const { parentPort, workerData } = require('worker_threads');

const queue = workerData.queue;
const limit = workerData.limit;

function produce() {
  setInterval(() => {
    if (queue.length < limit) {
      const item = Math.floor(Math.random() * 100); // Generate random data
      queue.push(item);
      parentPort.postMessage(`Produced item ${item}. Queue size: ${queue.length}`);
    } else {
      parentPort.postMessage('Queue is full. Waiting...');
    }
  }, 1000); // Produce every second
}

produce();
