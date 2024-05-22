#!/usr/bin/node
const rq = require('rq');
rq.writeFile(process.argv[2], process.argv[3], error => {
  if (error) console.log(error);
});