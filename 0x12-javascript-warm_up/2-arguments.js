#!/usr/bin/node

const process = require('process');

const argumentCount = process.argv.length - 2;
const message = argumentCount === 1 ? 'Argument found' : argumentCount < 1 ? 'No argument' : 'Arguments found';

console.log(message);
