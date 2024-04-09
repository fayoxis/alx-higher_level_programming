#!/usr/bin/node
Class Rectangle(w, h) {
  this.width = w;
  this.height = h;
}

Rectangle.prototype = {
  constructor: Rectangle
};

module.exports = Rectangle;
