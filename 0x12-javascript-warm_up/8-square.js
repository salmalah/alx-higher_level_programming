#!/usr/bin/node

const s = parseInt(process.argv[2]);
if (isNaN(s)) {
  console.log('Missing size');
} else if (s > 0) {
  for (let v = 0; v < s; v++) {
    let string = '';
    for (let j = 0; j < s; j++) {
      string += 'X';
    }
    console.log(string);
  }
}
