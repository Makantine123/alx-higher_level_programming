#!/usr/bin/node


const file1 = require('fs').readFileSync(process.argv[2], 'utf8');
const file2 = require('fs').readFileSync(process.argv[3], 'utf8');
fs.writeFileSync(process.argv[4], file1 + file2);
