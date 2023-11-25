#!/usr/bin/node
const array = require('./100-data').list;
console.log(array);
const map1 = array.map((currentElem, index) => currentElem * index);
console.log(map1);
