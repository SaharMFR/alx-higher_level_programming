#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const path = process.argv[3];

request.get(url, (err, response, contents) => {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(path, contents, 'utf-8', (err) => {
      if (err) console.log(err);
    });
  }
});
