#!/usr/bin/node
exports.esrever = function (list) {
  const newlist = [];
  for (let i = list.length - 1, j = 0; i >= 0; i--, j++) {
    newlist[j] = list[i];
  }
  return newlist;
};
