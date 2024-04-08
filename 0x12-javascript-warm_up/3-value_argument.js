#!/usr/bin/node
const process = require('process');
const message = 'No argument';

console.log(process.argv[2] === undefined ? message : process.argv[2]);
