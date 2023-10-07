#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const starwarsUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(starwarsUrl, (error, response, body) => {
  if (error) {
    return console.log(error);
  }
  const movieData = JSON.parse(body);
  console.log(movieData.title);
});
