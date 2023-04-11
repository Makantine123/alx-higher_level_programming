#!/usr/bin/node

const size = process.argv.length;
let myarr = [];

if (size < 3) {
  console.log('0');
} else if (size === 3) {
  console.log('0');
} else {
  myarr = process.argv.sort(function (a, b) {
    return b - a;
  });
  console.log(myarr[3]);
}
