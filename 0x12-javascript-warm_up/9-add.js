#!/usr/bin/node
const add = (a, b) => {
  return a + b;
};

const arg1 = Number(process.argv[2]);
const arg2 = Number(process.argv[3]);
console.log(add(arg1, arg2));
