#!/usr/bin/node
exports.esrever = function (list) {
    let newlist = [];
    for (let i = list.length - 1, j = 0; i >= 0; i--, j++)
    {
	newlist[j] = list[i];
    }
    return newlist;
};
