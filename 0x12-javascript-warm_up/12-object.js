#!/usr/bin/node
const myObject = {};
Object.assign(myObject, {
  type: 'object',
  value: 12
});

console.log(myObject);

myObject.value = 89;

console.log(myObject);
