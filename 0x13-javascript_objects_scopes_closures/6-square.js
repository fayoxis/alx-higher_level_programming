#!/usr/bin/node
const ParentSquare = require('./5-square.js');

class Square extends ParentSquare {
  constructor() {
    super();
  }

  charPrint(c) {
    if (typeof c === 'undefined') {
      this.print();
    } else {
      let square = '';
      for (let i = 0; i < this.width; i++) {
        square += c.repeat(this.width) + '\n';
      }
      console.log(square);
    }
  }
}

module.exports = Square;
