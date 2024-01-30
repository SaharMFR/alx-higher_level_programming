#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

const printed = {};
request.get(url, (err, response, data) => {
  if (err) {
    console.log(err);
  } else {
    const tasks = JSON.parse(data);
    for (let i = 0; i < tasks.length; i++) {
      if (tasks[i].completed) {
        if (printed[tasks[i].userId] === undefined) printed[tasks[i].userId] = 0;
        printed[tasks[i].userId]++;
      }
    }
    console.log(printed);
  }
});
