#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
myObject.incr = () => {
  myObject.value++;
};
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
