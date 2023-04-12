#!/usr/bin/node

let fs = require('fs');

let file1 = fs.readFileSync(process.argv[2], 'utf-8');
let file2 = fs.readFileSync(process.argv[3], 'utf-8');

fs.write(process.argv[4], file1 + file2);
