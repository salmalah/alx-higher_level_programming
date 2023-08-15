#!/usr/bin/node
exports.esrever = function (list) {
  const rev = [];
  for (let j = list.length - 1; j >= 0; j--) {
    rev.push(list[j]);
  }
  return rev;
};
