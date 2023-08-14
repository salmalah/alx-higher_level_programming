#!/usr/bin/node
const numberL = parseInt(process.argv[2]);
if (isNaN(numberL)) {
  console.log('Missing number of occurrences');
} else {
  for (let v = 0; v < numberL; v++) {
    console.log('C is fun');
  }
}
