#!/usr/bin/node
const first_arg = process.argv[2];
if (process.argv[2] === undefined || isNaN(first_arg)) {
  console.log('Missing size');
} else {
  const x = Number(first_arg);
  let i = 0;
  while (i < x) {
    console.log('X'.repeat(x));
    i++;
  }
}
