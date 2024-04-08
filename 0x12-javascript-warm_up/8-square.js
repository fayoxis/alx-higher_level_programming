#!/usr/bin/node
const n = Math.floor(Number(process.argv[2]));
if (isNaN(n)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < n; i++) {
    let line = '';
    for (let j = 0; j < n; j++) {
      line = line + 'X';
    }
    console.log(line);
  }
}
