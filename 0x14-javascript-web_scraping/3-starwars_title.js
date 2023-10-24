#!/usr/bin/node
const req = require('request');

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

req.get(url, (error, response, body) => {
  if (error) {
    console.error(error.message);
  } else {
    const movieData = JSON.parse(body);
    console.log(movieData.title);
  }
});
