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
    let width_of_Print = '';
    while (i < this.width) {
      width_of_Print = width_of_Print + 'X';
      i++;
    }
    while (j < this.height) {
      console.log(width_of_Print);
      j++;
    }
  }
}

module.exports = Rectangle;
