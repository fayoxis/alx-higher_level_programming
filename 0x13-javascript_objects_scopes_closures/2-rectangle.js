#!/usr/bin/node
module.exports = class {
  constructor(w, h) {
    this.setDimensions(w, h);
  }

  setDimensions(w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
};
