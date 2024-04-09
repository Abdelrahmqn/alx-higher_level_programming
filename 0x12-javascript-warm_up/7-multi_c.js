#!/usr/bin/node
const first_arg = process.argv[2];

if (first_arg === undefined || isNaN(first_arg)) {
  console.log('Missing number of occurrences');
} else {
  const temp = Number(first_arg);
  let i = 0;
  while (i < temp) {
    console.log('C is fun');
    i++;
  }
}
