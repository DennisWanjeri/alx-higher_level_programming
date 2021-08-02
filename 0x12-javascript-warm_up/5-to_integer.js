#!/usr/bin/node
const int_num = Math.floor(Number(process.argv[2]));
console.log(isNaN(int_num) ? 'Not a number' : `My number: ${int_num}`);
