#!/usr/bin/node
const x = Math.floor(Number(process.argv[2]));
const message1 = 'Missing number of occurrences';
const message2 = 'C is fun';

if (isNaN(x)) {
  console.log(message1);
} else {
  let i = x;
  while (i > 0) {
    console.log(message2);
    i--;
  }
}
