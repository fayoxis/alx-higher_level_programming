#!/usr/bin/node
module.exports = class Rectangle {
  constructor(width, height) {
    this.setSize(width, height);
  }

  setSize(w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
};
