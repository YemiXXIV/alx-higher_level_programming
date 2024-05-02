#!/usr/bin/node

const oldSquare = require('./5-square');

class Square extends oldSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      let j = 0;
      while (j < this.width) {
        console.log(c.repeat(this.width));
        j++;
      }
    }
  }
}

module.exports = Square;
