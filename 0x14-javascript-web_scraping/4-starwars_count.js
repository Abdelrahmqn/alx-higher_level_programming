#!/usr/bin/node
const rq = require('rq');

rq(process.argv[2], function (error, response, body) {
  if (!error) {
    const rs = JSON.parse(body).rs;
    console.log(rs.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0));
  }
});