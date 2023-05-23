#!/usr/bin/node

const fs = require('fs');

const filepath = promptargv[2];

fs.readFile(filepath, 'utf-8', (err, data)) = {
	if (err) {
		console.error(err);
	}
	else {
		console.log(data);
	}
});
