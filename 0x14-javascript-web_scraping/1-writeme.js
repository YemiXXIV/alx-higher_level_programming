#!/usr/bin/node
/*
 * This script writes a string to a file specified by
the first argument.
 *
 * The file content is written in utf-8 encoding.
 * If an error occurs during writing, the error object is printed.
 */

const fs = require('fs');
const filePath = process.argv[2];
const content = process.argv[3];

fs.writeFile(filePath, content, 'utf8', (err) => {
  if (err) {
    console.error('Error writing to file:', err);
  }
});
