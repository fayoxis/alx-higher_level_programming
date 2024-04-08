#!/usr/bin/node
const factorial = (n) => {
  if (n === 0 || isNaN(n)) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
};

const inputNumber = Number(process.argv[2]);
console.log(factorial(inputNumber));
