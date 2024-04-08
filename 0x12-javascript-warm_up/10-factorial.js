#!/usr/bin/node
function calculateFactorial(n) {
  return n === 0 || isNaN(n) ? 1 : n * calculateFactorial(n - 1);
}

const inputNumber = Number(process.argv[2]);
console.log(calculateFactorial(inputNumber));
