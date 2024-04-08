#!/usr/bin/node
const process = require('process');
const argument = process.argv[2];
const number = parseInt(argument);
const message = !isNaN(number) ? `My number: ${number}` : 'Not a number';

console.log(message);
