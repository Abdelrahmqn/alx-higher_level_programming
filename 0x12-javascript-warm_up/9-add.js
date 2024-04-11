#!/usr/bin/node
const first_arg = process.argv[2], second_arg = process.argv[3];
function add (a, b) {
    const Result = a + b;
    console.log(Result);
  }

  add(Number(first_arg), Number(second_arg));
