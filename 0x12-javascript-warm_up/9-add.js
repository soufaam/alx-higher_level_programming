#!/usr/bin/node
function facto (num) {
  if (num === 0) {
    return 1;
  }
  return num * facto(num - 1);
}
const number = parseInt(process.argv[2]);
if (isNaN(number)) {
  console.log(1);
} else {
  const f = facto(number);
  console.log(f);
}
