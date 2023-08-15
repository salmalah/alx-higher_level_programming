#!/usr/bin/node
const fs = require('fs');
const f1Path = process.argv[2];
const f2Path = process.argv[3];
const destPath = process.argv[4];
const f1Content = fs.readFileSync(f1Path, 'utf8');
const f2Content = fs.readFileSync(f2Path, 'utf8');
const concat = f1Content + f2Content;
fs.writeFileSync(destPath, concat);
