#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (!Number.isInteger(w) || w <= 0 || !Number.isInteger(h) || h <= 0) {
      {}
    } else {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
