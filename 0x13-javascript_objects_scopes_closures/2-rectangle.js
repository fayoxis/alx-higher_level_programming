#!/usr/bin/node
class Rectangle {
  constructor(width, height) {
    this.width = width;
    this.height = height;
  }

  static create(width, height) {
    if (width > 0 && height > 0) {
      return new Rectangle(width, height);
    }
    return null;
  }
}

module.exports = Rectangle;
