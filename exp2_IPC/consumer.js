const { parentPort, workerData } = require('worker_threads');

const queue = workerData.queue;

function consume() {
  setInterval(() => {
    if (queue.length > 0) {
      const item = queue.shift(); // Remove the first item from the queue
      parentPort.postMessage(`Consumed item ${item}. Queue size: ${queue.length}`);
    } else {
      parentPort.postMessage('Queue is empty. Waiting...');
    }
  }, 1500); // Consume every 1.5 seconds
}

consume();
