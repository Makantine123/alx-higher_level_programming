#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let shape = '';
    for (let i = 0; i < this.width; i++) {
      shape = shape + 'X';
    }
    for (let k = 0; k < this.height; k++) {
      console.log(shape);
    }
  }
};
