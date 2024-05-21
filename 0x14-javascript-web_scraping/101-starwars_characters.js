#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, function (error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    let index = 0;

    do {
      request(characters[index], function (error, response, body) {
        if (!error) {
          console.log(JSON.parse(body).name);
        }
      });
      index++;
    } while (index < characters.length);
  }
});
