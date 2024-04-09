#!/usr/bin/node
const argvs = process.argv[2];
if (argvs === undefined)
{
  console.log('No argument');
} else {
  console.log(argvs);
}
