#!/usr/bin/node
module.exports = {
  converter: function(base) {
    return function(num) {
      return num.toString(base);
    };
  }
};
