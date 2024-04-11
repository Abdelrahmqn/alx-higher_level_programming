#!/usr/bin/node
const arg = process.argv[1];
if (isNaN(arg) || arg === undefined) {
  console.log('Not a number');
} else {
  console.log('My number:', arg);
}
