#!/usr/bin/node
module.exports = class Rectangle {
  #width;
  #height;

  constructor(width, height) {
    this.setDimensions(width, height);
  }

  setDimensions(width, height) {
    if (width > 0 && height > 0) {
      this.#width = width;
      this.#height = height;
    }
  }

  get width() {
    return this.#width;
  }

  get height() {
    return this.#height;
  }
};
