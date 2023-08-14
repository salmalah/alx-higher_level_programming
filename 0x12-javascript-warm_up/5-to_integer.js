#!/usr/bin/node
const value = process.argv[2];
const valueInt = parseInt(value);
if (!isNaN(valueInt)) {
  console.log('My number:', valueInt);
} else {
  console.log('Not a number');
}
