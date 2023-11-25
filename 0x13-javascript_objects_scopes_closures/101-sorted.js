#!/usr/bin/node
const dict = require('./101-data').dict;
const dic = {};
const values = Object.values(dict).sort();
const uniq = [];
for (const elemet of values) {
  if (!uniq.includes(elemet)) {
    uniq.push(elemet);
  }
}
for (let index = 0; index < uniq.length; index++) {
  const arr = [];
  for (const key in dict) {
    if (uniq[index] === dict[key]) {
      arr.push(key);
    }
  }
  dic[uniq[index]] = arr;
}
console.log(dic);
