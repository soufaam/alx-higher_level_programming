#!/usr/bin/node
const Square5 = require('./5-square');
class Square extends Square5 {
  charPrint (c) {
    let symb;
    if (c === undefined) {
      symb = 'X';
    } else {
      symb = c;
    }
    let string = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        string += symb;
      }
      if (i === this.height - 1) {
        break;
      }
      string += '\n';
    }
    console.log(string);
  }
}
module.exports = Square;
