#!/usr/bin/node

const sqs = parseInt(process.argv[2]);
let shape = '#';

if (!Number.isInteger(sqs)) {
  console.log('Missing size');
} else {
  for (let v = 0; v < sqs; v++) {
    shape = shape + '#';
  }

  for (let i = 0; i < sqs; i++) {
    console.log(shape);
  }
}
