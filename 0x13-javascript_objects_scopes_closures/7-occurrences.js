#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let x = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      x += 1;
    }
  }
  return x;
};
