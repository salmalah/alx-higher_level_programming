#!/usr/bin/node
const request = require('request');
const APIurl = process.argv[2];
const eighteen = '18';

request.get(APIurl, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  if (response && response.statusCode !== 200) {
    console.error('status code:', response.statusCode);
    return;
  }
  const filmsData = JSON.parse(body);
  let wedgeAntillesFilms = 0;
  filmsData.results.forEach(film => {
    for (const c of film.characters) { if (c.includes(eighteen)) wedgeAntillesFilms++; }
  });
  console.log(wedgeAntillesFilms);
});
