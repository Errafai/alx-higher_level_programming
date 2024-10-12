#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }
  print() {
      while (h--) {
          console.log(this.width * "X");
      }
}

module.exports = Rectangle;
