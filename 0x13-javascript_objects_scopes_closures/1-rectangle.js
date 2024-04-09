#!/usr/bin/node
class Rectangle {
  constructor(w, h) {
    this._width = w;
    this._height = h;
  }

  get width() {
    return this._width;
  }

  set width(value) {
    this._width = value;
  }

  get height() {
    return this._height;
  }

  set height(value) {
    this._height = value;
  }
}

module.exports = Rectangle;
