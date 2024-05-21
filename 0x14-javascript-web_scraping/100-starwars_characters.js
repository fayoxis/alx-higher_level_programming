#!/usr/bin/node

const axios = require('axios');

const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';

async function getCharacterNames() {
  try {
    const response = await axios.get(`${url}${id}`);
    const { characters } = response.data;

    const characterNames = await Promise.all(
      characters.map(async (characterUrl) => {
        const characterResponse = await axios.get(characterUrl);
        return characterResponse.data.name;
      })
    );

    characterNames.forEach(name => console.log(name));
  } catch (error) {
    console.error(error);
  }
}

getCharacterNames();
