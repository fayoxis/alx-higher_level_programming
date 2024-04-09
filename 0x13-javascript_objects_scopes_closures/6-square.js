#!/usr/bin/node
module.exports = class Square extends require('./5-square.js') {
  charPrint(c) {
    if (c === undefined) {
      this.print();
    } else {
      let output = '';
      for (let i = 0; i < this.height; i++) {
        output += c.repeat(this.width) + '\n';
      }
      console.log(output);
    }
  }
}
