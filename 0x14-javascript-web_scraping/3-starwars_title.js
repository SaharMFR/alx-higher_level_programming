#!/usr/bin/node

const request = require('request');
const epNum = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + epNum;

request.get(url, (err, response, body) => {
  if (err) console.log(err);
  else console.log((JSON.parse(body)).title);
});
