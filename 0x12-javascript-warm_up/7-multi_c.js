#!/usr/bin/node
let x;
let i = 1;
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Missing number of occurrences');
} else {
  x = Number(process.argv[2]);
  while (i <= x) {
    i++;
    console.log('C is fun');
  }
}
