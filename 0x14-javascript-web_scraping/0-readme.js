#!/usr/bin/node
/*
 * This script reads and prints the content of a file specified by
 * the first argument.
 *
 * The file content is read in utf-8 encoding.
 * If an error occurs during reading, the error object is printed.
 */

const fs = require('fs');
const filePath = process.argv[2];

if (!filePath) {
  console.error(`Usage: ${process.argv[1]} <file_path>`);
  process.exit(1);
}

fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.error('Error reading file:', err);
    return;
  }
  console.log(data);
});
