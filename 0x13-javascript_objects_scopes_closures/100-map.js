#!/usr/bin/node
const list = require('./100-data.js').list;

console.log(list);
const my_list = list.map((value, index) => value * index);
console.log(my_list);
