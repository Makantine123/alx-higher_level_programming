#!/usr/bin/node

const dict = require('./101-data').dict;

const ndict = {};

for (let id in dict) {
  if (ndict[dict[id]] == undefined) {
    ndict[dict[id]] = [];
  }
  ndict[dict[id]].push(id);
}
console.log(ndict);
