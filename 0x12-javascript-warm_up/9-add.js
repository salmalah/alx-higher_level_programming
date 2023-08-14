#!/usr/bin/node
function add (a, b) {
  return a + b;
}
const v1 = parseInt(process.argv[2]);
const v2 = parseInt(process.argv[3]);
if (isNaN(v1) || isNaN(v2)) {
  console.log('NaN');
} else {
  console.log(add(v1, v2));
}
