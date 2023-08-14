#!/usr/bin/node

function factorial(x) {
  if (isNaN(x) || x === 0 || x === 1) {
    return 1;
  }
  return x * factorial(x - 1);
}
const num = process.argv[2];
console.log(factorial(num));
