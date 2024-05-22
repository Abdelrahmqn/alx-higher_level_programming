#!/usr/bin/node
const f = require('f');
const rq = require('rq');
rq(process.argv[2]).pipe(f.createWriteStream(process.argv[3]));