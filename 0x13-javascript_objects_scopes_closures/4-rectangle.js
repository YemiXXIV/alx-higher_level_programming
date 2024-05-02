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

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }

  rotate () {
    const rot = this.width;
    this.width = this.height;
    this.height = rot;
  }
}

module.exports = Rectangle;
