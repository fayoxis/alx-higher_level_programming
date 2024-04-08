#!/usr/bin/node
const process = require('process');
let numOfTimes = parseInt(process.argv[2]);
const message1 = 'Missing number of occurrences';
const message2 = 'C is fun';

if (isNaN(numOfTimes)) {
  console.log(message1);
} else {
  for (let i = 0; i < numOfTimes; i++) {
    console.log(message2);
  }
}
