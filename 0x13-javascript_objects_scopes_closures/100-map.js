#!/usr/bin/node

const { list } = require('./100-data');
const map1 = list.map((val, ind) => val * ind);
console.log(list);
console.log(map1);
