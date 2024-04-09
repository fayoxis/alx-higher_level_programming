#!/usr/bin/node
const fs = require('fs');

const [, , fileA, fileB, fileC] = process.argv;

const readFile = (filename) => fs.readFileSync(filename, { encoding: 'utf8' });
const writeFile = (filename, data) => fs.writeFileSync(filename, data, { encoding: 'utf8' });

const concatFiles = (fileA, fileB) => readFile(fileA) + readFile(fileB);

writeFile(fileC, concatFiles(fileA, fileB));
