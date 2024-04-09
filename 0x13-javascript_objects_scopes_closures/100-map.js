#!/usr/bin/node
const { list } = require('./100-data.js');

console.log(list);
console.log(list.map((item, index) => item * index));
