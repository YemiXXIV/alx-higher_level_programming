#!/usr/bin/node

function add (a, b) {
  return a + b;
}

const addition = add(parseInt(process.argv[2]), parseInt(process.argv[3]));

console.log(addition);
