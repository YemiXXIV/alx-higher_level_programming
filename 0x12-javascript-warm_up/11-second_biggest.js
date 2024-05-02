#!/usr/bin/node

let i = 2;
let j;
let Numberslist;
let theList;

if (process.argv.length < 4) {
  console.log(0);
} else {
  Numberslist = [];
  while (process.argv[i] !== undefined) {
    Numberslist.push(parseInt(process.argv[i]));
    i++;
  }

  Numberslist.sort((a, b) => b - a);

  theList = [Numberslist[0]];
  j = 1;
  while (Numberslist[j]) {
    if (Numberslist[j - 1] !== Numberslist[j]) {
      theList.push(parseInt(Numberslist[j]));
    }
    j++;
  }
  console.log(theList[1]);
}
