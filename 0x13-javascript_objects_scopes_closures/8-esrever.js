#!/usr/bin/node

module.exports.esrever = function (list) {
  const nlist = [];
  let j = 0;

  for (let i = list.length - 1; i >= 0; i--, j++) {
    nlist[j] = list[i];
  }
  return (nlist);
};
