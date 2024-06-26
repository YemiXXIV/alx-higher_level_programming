#!/usr/bin/node

/*
 * This script fetches and prints the number of movies
 * where the character "Wedge Antilles"
 * (character ID 18) is present.
 */

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, function (error, response, body) {
  const films = JSON.parse(body).results;
  let count = 0;

  films.forEach(film => {
    film.characters.forEach(characterUrl => {
      if (characterUrl.includes('/18/')) {
        count++;
      }
    });
  });
  console.log(count);
  if (error) {
    console.error('Error:', error);
  }
});
