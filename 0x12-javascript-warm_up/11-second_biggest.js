#!/usr/bin/node
if (isNaN(process.argv[2]) || process.argv[2] === 1) {
  console.log(0);
} else {
  const PRocess = process.argv.map(Number)
    .slice(2, process.argv.length)
    .sort((a, b) => a - b);
  console.log(PRocess[PRocess.length - 2]);
}
