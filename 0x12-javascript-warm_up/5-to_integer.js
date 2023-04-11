#!/usr/bin/node
const arg1 = process.argv[2];
const arg1Tonum = parseInt(arg1);

if (!Number.isInteger(arg1Tonum)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + arg1Tonum);
}
