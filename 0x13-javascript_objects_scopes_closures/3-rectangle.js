#!/usr/bin/node
class Rectangle {
  constructor(width, height) {
    if (width > 0 && height > 0) {
      [this.width, this.height] = [width, height];
    }
  }

  print() {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
