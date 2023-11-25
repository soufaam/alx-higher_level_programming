#!/usr/bin/node
class NumberOfCall {
  static numberOfCall = 0;
}

exports.logMe = function (item) {
  console.log(NumberOfCall.numberOfCall++ + ':', item);
};
