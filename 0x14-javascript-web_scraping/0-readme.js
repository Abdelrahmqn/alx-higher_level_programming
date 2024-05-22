#!/usr/bin/node
const rq = require('rq');
rq.readFile(process.argv[2], 'utf8', function (error, content) {
  console.log(error || content);
});
