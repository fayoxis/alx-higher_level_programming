#!/usr/bin/node
const lenght = Math.floor(Number(process.argv[2]));
if (isNaN(lenght)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < lenght; i++) {
    let line = '';
    for (let j = 0; j < lenght; j++) {
      line = line + 'X';
    }
    console.log(line);
  }
}
