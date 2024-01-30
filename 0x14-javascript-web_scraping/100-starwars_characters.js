#!/usr/bin/node

const request = require('request');
const movieID = process.argv[2];
const api = 'https://swapi-api.alx-tools.com/api/films/' + movieID;

request.get(api, (err, response, data) => {
  if (err) {
    console.log(err);
  } else {
    const chars = JSON.parse(data).characters;
    for (const character of chars) {
      request(character, (err, response, data) => {
        if (err) console.log(err);
        else console.log(JSON.parse(data).name);
      });
    }
  }
});
