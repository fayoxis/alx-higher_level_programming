#!/usr/bin/node
exports.nbOccurences = function(list, searchElement) {
  return list.reduce((count, currentElement) => {
    return currentElement === searchElement ? count + 1 : count;
  }, 0);
};
