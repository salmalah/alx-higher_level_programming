#!/usr/bin/node

const request = require('request');
const eighteen = 'https://swapi-api.alx-tools.com/api/people/18/'
const url = process.argv[2];

request.get(url, (err, response, body) => {
  if (error) {
    console.error(err.message);
  } else {
    const filmsData = JSON.parse(body).results;
    const wedgeAntillesMovies = filmsData.filter(film =>
      film.characters.includes(eighteen)
    );
    console.log(wedgeAntillesMovies.length);
  }
});
