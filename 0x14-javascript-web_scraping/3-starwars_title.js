#!/usr/bin/node
const axios = require('axios');
const episodeNum = process.argv[2];
const API_URL = 'https://swapi-api.hbtn.io/api/films/';
axios.get(API_URL + episodeNum)
  .then(response => {
    console.log(response.data.title);
  })
  .catch(error => {
    if (error.response) {
      console.log('Error code: ' + error.response.status);
    } else {
      console.log(error);
    }
  });
