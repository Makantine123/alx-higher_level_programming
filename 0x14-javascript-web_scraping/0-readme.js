#!/usr/bin/node
// Script reads and prints the content of a file

const fs = require('fs');
const filepath = promptargv[2];

fs.readFile(filepath, 'utf-8', (error, data)) = {
	if (error) {
		console.log(error);
	} else {
		console.log(data);
	}
});
