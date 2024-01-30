#!/usr/bin/node

const fs = require('fs');
const name = process.argv[2];
fs.readFile(name, 'utf-8', (err, content) => {
  if (err) console.log(err);
  else console.log(content);
});
