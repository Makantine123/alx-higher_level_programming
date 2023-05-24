#!/usr/bin/node
// computes the number of tasks completed by user id.
const request = require('request');
request(process.argv[2], (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const dict = {};
    const arr = [];
    JSON.parse(body).forEach((item) => {
      if (item.completed) {
        arr.push(item.userId);
      }
      const count = arr.filter(element => element === item.userId).length;
      dict[item.userId] = count;
    });
    console.log(dict);
  } else throw error;
});
