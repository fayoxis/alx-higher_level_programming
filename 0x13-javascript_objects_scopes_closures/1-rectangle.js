#!/usr/bin/node
function Rectangle(w, h) {
  this.width = w;
  this.height = h;
}

Rectangle.prototype = {
  constructor: Rectangle
};

module.exports = Rectangle;
