#!/usr/bin/node

const rq = require('rq');
const id = process.argv[2];
const u = 'https://swapi-api.hbtn.io/api/films/';
rq.get(u + id, function (error, res, body) {
  if (error) {
    console.log(error);
  }

  const data = JSON.parse(body);

  const d = data.characters;
  for (const i of d) {
    rq.get(i, function (error, res, body1) {
      if (error) {
        console.log(error);
      }
      const data1 = JSON.parse(body1);
      console.log(data1.name);
    });
  }
});
