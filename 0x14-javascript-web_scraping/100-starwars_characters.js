#!/usr/bin/node
const axios = require('axios');

const filmId = process.argv[2];
const filmUrl = `https://swapi-api.alx-tools.com/api/films/${filmId}`;

async function fetchCharacterNames() {
  try {
    // Fetch the film data
    const filmResponse = await axios.get(filmUrl);
    const { characters } = filmResponse.data;

    // Fetch the character data for each character URL
    const characterNames = await Promise.all(characters.map(async (characterUrl) => {
      const characterResponse = await axios.get(characterUrl);
      return characterResponse.data.name;
    }));

    // Print the character names
    characterNames.forEach(name => console.log(name));
  } catch (error) {
    console.error(error);
  }
}

fetchCharacterNames();
