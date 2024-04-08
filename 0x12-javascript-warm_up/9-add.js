#!/usr/bin/node
const args = process.argv.slice(2);
const a = Number(args[0]);
const b = Number(args[1]);

function add(a, b) {
  return a + b;
}

console.log(add(a, b));
