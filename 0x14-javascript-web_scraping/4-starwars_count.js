#!/usr/bin/node

const request = require('request');
furl = process.argv[2];

request.get(furl, function (err, response, body) {
    if (!err) {
        const results = JSON.parse(body).results;
        console.log(results.reduce((count, movie) => {
          return movie.characters.find((character) => character.endsWith('/18/'))
            ? count + 1
            : count;
        }, 0));
    }
});
