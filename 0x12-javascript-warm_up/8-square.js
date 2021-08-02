#!/usr/bin/node
const size = Math.floor(Number(process.argv[2]));
if (isNaN(size)) {
    console.log('Missing size');
} else {
    for (let row = 0; row < size; row++) {
	let row_str = '';
	for (let c = 0; c < size; c++) row_str += 'X';
	console.log(row_str);
    }
}