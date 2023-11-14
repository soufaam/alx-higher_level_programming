#!/usr/bin/node
const argv = process.argv;
if (argv.length === 2) {
  console.log(0);
} else if (argv.length === 3) {
  console.log(0);
} else {
  const number1 = parseInt(argv[2]);
  const number2 = parseInt(argv[3]);
  let big, secbig;
  if (number1 > number2) {
    big = number1;
    secbig = number2;
  } else {
    big = number2;
    secbig = number1;
  }
  for (let j = 4; j < argv.length; j++) {
    const num = parseInt(argv[j]);
    if (big < num) {
      secbig = big;
      big = num;
    } else if (secbig < num) {
      secbig = num;
    }
  }
  console.log(secbig);
}
