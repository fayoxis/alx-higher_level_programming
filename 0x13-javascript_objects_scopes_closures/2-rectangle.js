#!/usr/bin/node
//  class `Rectangle` that makes a rectangle, by  filtering
class Rectangle {
  constructor(w, h) {
    if (w > 0 && h > 0) {
      [this.width, this.height] = [w, h];
    }
  }
}

module.exports = Rectangle;
