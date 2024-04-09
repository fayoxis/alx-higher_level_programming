#!/usr/bin/node
exports.nbOccurrences = function(list, searchElement) {
  return list.reduce((count, current) => {
    if (current === searchElement) {
      return count + 1;
    } else {
      return count;
    }
  }, 0);
};
