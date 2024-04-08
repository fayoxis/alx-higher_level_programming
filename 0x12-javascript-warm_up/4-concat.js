#!/usr/bin/node
const process = require('process');
const args = process.argv.slice(2);
const output = args.length === 2 ? `${args[0]} is ${args[1]}` : '';

console.log(output);
