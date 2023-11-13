#!/usr/bin/node
const argv = process.argv;
if (argv.length === 2) {
  console.log(0);
} else if (argv.length === 3) {
  console.log(0);
} else {
  let big = parseInt(argv[2]);
  let secbig = parseInt(argv[3]);
  for (let j = 2; j < argv.length; j++) {
    const num = parseInt(argv[j]);
    if (big < num) {
      secbig = big;
      big = num;
    }
  }
  console.log(secbig);
}
