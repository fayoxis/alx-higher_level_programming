#!/usr/bin/node
exports.converter = base => {
  return num => num.toString(base);
};
