#!/usr/bin/node
class MyObject {
  constructor() {
    this.type = 'object';
    this.value = 12;
  }

  incr() {
    this.value++;
  }
}

const myObject = new MyObject();
console.log(myObject);

myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
