#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
let count = 0;

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const res = (JSON.parse(body)).results;
    for (let i = 0; i < res.length; i++) {
      const chars = res[i].characters;
      for (let j = 0; j < chars.length; j++) {
        if (chars[j].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
