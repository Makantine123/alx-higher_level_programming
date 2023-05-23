#!/usr/bin/node
// Script reads and prints the content of a file

const fs = require('fs');
const file = process.argv[2];

fs.readFile(file, 'utf-8', function (error, data) {
	if (error) {
		console.log(error);
	} else {
		console.log(data);
	}
});
