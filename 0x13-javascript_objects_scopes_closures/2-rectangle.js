#!/usr/bin/node
module.exports = class Rectangle {
  constructor(width, height) {
    this.setDimensions(width, height);
  }

  setDimensions(width, height) {
    if (width > 0 && height > 0) {
      this.width = width;
      this.height = height;
    }
  }
};
