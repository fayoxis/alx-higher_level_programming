#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};

console.log(myObject);

function increaseValue() {
  myObject.value++;
}

increaseValue();
console.log(myObject);
increaseValue();
console.log(myObject);
increaseValue();
console.log(myObject);
