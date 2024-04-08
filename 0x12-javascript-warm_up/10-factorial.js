#!/usr/bin/node
function factorial (num) {
  return num === 0 || isNaN(num) ? 1 : num * factorial(num - 1);
}

console.log(factorial(Number(process.argv[2])));
