#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      const s = 'X'.repeat(this.width);
      console.log(s);
    }
  }

  rotate() {
      this.height = this.width + this.height;
      this.width = this.height - this.width;
      this.height = this.height - this.width;
  }
  
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
