#!/usr/bin/node
const data = require('./100-data');
const init = data.list;
const newL = init.map((value, index) => value * index);
console.log(init);
console.log(newL);
