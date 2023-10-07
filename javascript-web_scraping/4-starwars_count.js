#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    return console.log(error);
  }

  const movieData = JSON.parse(body);
  let count = 0;

  for (const movie of movieData.results) {
    if (movie.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
      count++;
    }
  }
  console.log(count);
});
