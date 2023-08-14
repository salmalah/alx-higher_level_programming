#!/usr/bin/node
const argl = process.argv[2];
if (argl === undefined) {
  console.log('No argument');
} else {
  console.log(argl);
}
