#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};

console.log(myObject);

function incr(obj) {
  obj.value++;
}

incr(myObject);
console.log(myObject);
incr(myObject);
console.log(myObject);
incr(myObject);
console.log(myObject);
