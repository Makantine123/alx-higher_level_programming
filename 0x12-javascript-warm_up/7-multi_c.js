#!/usr/bin/node

const arg1 = process.argv[2];
const arg1Tonum = parseInt(arg1);

if (!Number.isInteger(arg1Tonum)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < arg1Tonum; i++) {
    console.log('C is fun');
  }
}
