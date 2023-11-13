#!/usr/bin/node
const size = parseInt(process.argv[2]);
let string = '';
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j++) {
      string += 'X';
    }
    if (i === size - 1) {
      break;
    }
    string += '\n';
  }
  console.log(string);
}
