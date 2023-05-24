#!/usr/bin/node
// Reads and prints contents of a file
const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', function (error, data) {
  if (data === undefined) {
    console.log(error);
  }	else {
    console.log(data);
  }
});
