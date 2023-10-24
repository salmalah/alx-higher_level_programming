#!/usr/bin/node
const request = require('request');

const MovieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${MovieId}`;

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const charac = JSON.parse(body).characters;
  charac.forEach((url) => {
    request.get(url, (error, response, body) => {
      if (err) {
        console.log(err);
        return;
      }
      console.log(JSON.parse(body).name);
    });
  });
});
