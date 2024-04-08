#!/usr/bin/node
function factorial(number) {
  if (number > 1) {
    return number * factorial(number - 1);
  } else {
    return 1;
  }
}

const n = Math.floor(Number(process.argv[2]));
const result = factorial(n);
console.log(result);
