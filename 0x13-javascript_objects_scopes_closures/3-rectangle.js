#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i = 0;
    let j = 0;
    let printWidth = '';
    while (i < this.width) {
      printWidth = printWidth + 'X';
      i++;
    }
    while (j < this.height) {
      console.log(printWidth);
      j++;
    }
  }
}

module.exports = Rectangle;
