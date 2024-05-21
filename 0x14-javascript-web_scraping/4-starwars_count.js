#!/usr/bin/node
const axios = require('axios');
let num = 0;
async function fetchFilmCount() {
  try {
    const response = await axios.get(process.argv[2]);
    const { results } = response.data;

    results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes('18')) {
          num += 1;
        }
      });
    });

    console.log(num);
  } catch (error) {
    console.error(error);
  }
}
fetchFilmCount();
