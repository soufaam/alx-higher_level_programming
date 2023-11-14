#!/usr/bin/node
exports.esrever = function (list) {
  const revers = [];
  for (let j = list.length - 1; j >= 0; j--) {
    revers[list.length - 1 - j] = list[j];
  }
  return revers;
};
