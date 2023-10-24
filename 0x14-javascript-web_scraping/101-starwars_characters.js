#!/usr/bin/node
const request = require('request');

const MovieId = process.argv[2];
const APIurl = `https://swapi-api.alx-tools.com/api/films/${MovieId}`;

function requestPromise (APIurl) {
  return new Promise((resolve, reject) => {
    request.get(APIurl, (err, response, body) => {
      if (err) reject(err);
      else resolve(body);
    });
  });
}

async function printCharac () {
  try {
    const body = await requestPromise(APIurl);
    const charc = JSON.parse(body).characters;

    for (let i = 0; i < charc.length; i++) {
      const characterBody = await requestPromise(charc[i]);
      console.log(JSON.parse(characterBody).name);
    }
  } catch (error) {
    console.error(error);
  }
}

printCharac();
