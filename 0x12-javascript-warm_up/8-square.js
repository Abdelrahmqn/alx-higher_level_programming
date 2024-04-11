#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  let i = 0;
  while (i < Number(process.argv[2])) {
    console.log('X'.repeat(Number(process.argv[2])));
    i++;
  }
}
