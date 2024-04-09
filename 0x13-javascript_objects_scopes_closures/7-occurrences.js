#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.reduce(function (count, current) {
    return current === searchElement ? count + 1 : count
  }, 0)
}
