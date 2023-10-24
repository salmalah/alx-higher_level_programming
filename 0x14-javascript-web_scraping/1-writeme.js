#!/usr/bin/node
const fs = require('fs');

const filePath = process.argv[2];
const stringContent = process.argv[3];

fs.writeFile(filePath, stringContent, 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
});
