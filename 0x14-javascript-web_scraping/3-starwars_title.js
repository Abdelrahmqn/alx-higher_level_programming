#!/usr/bin/node

const rq = require('rq');
const epN = process.argv[2];
const api_rl = 'https://swapi-api.hbtn.io/api/films/';
rq(api_rl + epN, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const responseJS = JSON.parse(body);
    console.log(responseJS.title);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});