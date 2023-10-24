#!/usr/bin/node
const fs = require('fs');

const filePath = process.argv[2];
const string_content = process.argv[3];

fs.writeFile(filePath, string_content, 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
});
