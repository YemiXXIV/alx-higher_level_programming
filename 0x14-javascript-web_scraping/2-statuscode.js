#!/usr/bin/node
/*
 * This script performs a GET request to a specified
 * URL and prints the status code of the response.
 */

const request = require('request');

const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.error('code: ${response.statusCode}');
  }
});
