#!/usr/bin/node
class Rectangle {
  constructor(w, h) {
    this.width = w > 0 ? w : 0;
    this.height = h > 0 ? h : 0;
  }

  print() {
    const row = 'X'.repeat(this.width);
    for (let i = 0; i < this.height; i++) {
      console.log(row);
    }
  }

  rotate() {
    [this.width, this.height] = [this.height, this.width];
  }

  double() {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
