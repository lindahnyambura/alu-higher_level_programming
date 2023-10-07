#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    return console.log(error);
  }

  fs.writeFile(filePath, body, 'utf8', function (err) {
    if (err) {
      return console.log(err);
    }
  });
});
