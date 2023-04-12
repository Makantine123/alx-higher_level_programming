#!/usr/bin/node

const saquareParent = require('./5-square');

module.exports = class Square extends saquareParent {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let k = 0; k < this.height; k++) {
      console.log(c.repeat(this.width));
    }
  }
};
