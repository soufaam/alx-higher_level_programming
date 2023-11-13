#!/usr/bin/node
if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing number of occurrences');
} else {
  let it = 0;
  for (it; it < parseInt(process.argv[2]); it++) {
    console.log('C is fun');
  }
}
