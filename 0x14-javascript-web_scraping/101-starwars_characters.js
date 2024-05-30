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

  fetchCharactersSequentially(characterUrls);
});

function fetchCharactersSequentially (urls) {
  const fetchCharacterName = (url) => {
    return new Promise((resolve, reject) => {
      request(url, function (error, response, body) {
        if (error) {
          reject(error);
          return;
        }
        const character = JSON.parse(body);
        resolve(character.name);
      });
    });
  };

  urls.reduce((promiseChain, currentUrl) => {
    return promiseChain.then(() => {
      return fetchCharacterName(currentUrl).then((name) => {
        console.log(name);
      });
    });
  }, Promise.resolve());
}
