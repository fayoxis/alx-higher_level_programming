#!/usr/bin/node
const lenght = Math.floor(Number(process.argv[2]));
if (isNaN(lenght)) {
  console.log('Missing size');
} else {
  for (let r = 0; r < lenght; r++) {
    let row = '';
    for (let c = 0; c < lenght; c++) row += 'X';
    console.log(row);
  }
