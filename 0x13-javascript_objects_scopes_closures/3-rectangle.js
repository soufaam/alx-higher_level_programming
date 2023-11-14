#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (Number.isInteger(w) && w > 0 && Number.isInteger(h) && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let string = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        string += 'X';
      }
      if (i === this.height - 1) {
        break;
      }
      string += '\n';
    }
    console.log(string);
  }
}
module.exports = Rectangle;
