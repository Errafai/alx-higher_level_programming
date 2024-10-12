#!/usr/bin/node
const Rectangle = require('./4-rectangle.js');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.width; i++) {
        const s = c.repeat(this.width);
        console.log(s);
      }
    } else {
      super.print();
    }
  }
}

module.exports = Square;
