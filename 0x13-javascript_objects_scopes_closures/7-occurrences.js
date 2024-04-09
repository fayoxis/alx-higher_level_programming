#!/usr/bin/node
exports.nbOccurrences = function(list, searchElement) {
  return list.filter(element => element === searchElement).length;
};
