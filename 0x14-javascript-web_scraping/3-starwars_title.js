#!/usr/bin/node
/*
 * This script fetches and prints the title of a Star
 * Wars movie based on the given episode number.
 */

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, function (error, response, body) {
  console.log(error || JSON.parse(body).title);
});
