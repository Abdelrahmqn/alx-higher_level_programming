#!/usr/bin/node
function add (a, b) {
  const Result = a + b;
  console.log(Result);
}

add(Number(process.argv[2]), Number(process.argv[3]));
