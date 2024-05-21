#!/usr/bin/node
const http = require('http');
const url = process.argv[2];
http.get(url, (response) => {
  console.log(`code: ${response.statusCode}`);
});
