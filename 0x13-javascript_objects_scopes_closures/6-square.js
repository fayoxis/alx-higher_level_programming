#!/usr/bin/node
const Rectangle = require('./5-rectangle');

class Square extends Rectangle {
  /**
   * @method charPrint - prints the square using the character c
   * @param {string} c - the character to print the square with (default: 'X')
   * @returns {void}
   */
  charPrint(c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let s = '';
      for (let j = 0; j < this.width; j++) {
        s += c;
      }
      console.log(s);
    }
  }
}

module.exports = Square;
