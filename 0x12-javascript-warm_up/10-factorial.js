#!/usr/bin/node

const n= parseInt(process.argv[2]);
let result = 1;

if (isNaN(n)) {
  console.log(1);
} else {
  console.log(factorial(n));
}

function factorial (a) {
  if (a < 1) {
    return result;
  } else {
    result = a * factorial(a - 1);
    return result;
  }
}
