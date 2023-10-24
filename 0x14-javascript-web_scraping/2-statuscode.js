#!/usr/bin/node
const req = require('request');

const url = process.argv[2];

req.get(url, (error, response) => {
  if (error) {
    console.error(error.message);
  } else {
    console.log('code:', response.statusCode);
  }
});
