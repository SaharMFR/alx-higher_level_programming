#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request.get(url, (err, response, data) => {
  if (err) {
    console.log(err);
  } else {
    const chars = JSON.parse(data).characters;
    charsInOrder(chars, 0);
  }
});

const charsInOrder = function (chars, i) {
  if (i === chars.length) return;
  request(chars[i], (err, response, data) => {
    if (err) {
      console.log(err);
    } else {
      console.log(JSON.parse(data).name);
      charsInOrder(chars, ++i);
    }
  });
};
