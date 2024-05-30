#!/usr/bin/node

/*
 * This script fetches and prints the names of all characters
 * in a given Star Wars movie based on the provided movie ID.
 */

const request = require('request');

const movieId = process.argv[2];
const urls = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(urls, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
    return;
  }

  const film = JSON.parse(body);
  const characterUrls = film.characters;

  characterUrls.forEach(url => {
    request(url, function (error, response, body) {
      if (error) {
        console.error('Error:', error);
        return;
      }

      const character = JSON.parse(body);
      console.log(character.name);
    });
  });
});
