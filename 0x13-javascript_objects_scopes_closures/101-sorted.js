#!/usr/bin/node
const dt = require('./101-data');
const originalD = dt.dict;
const newD = {};
for (const usId in originalD) {
  const occurrences = originalD[usId];
  if (!newD[occurrences]) {
    newD[occurrences] = [];
  } 
  newD[occurrences].push(usId);
}
console.log(newD);
