#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  let counter = 0;
  while (counter < x) {
    theFunction();
    counter++;
  }
};
