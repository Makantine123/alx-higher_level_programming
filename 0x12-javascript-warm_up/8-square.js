#!/usr/bin/node

const sqs = parseInt(process.argv[2]);
let shape = '#';

if (!Number.isInteger(sqs)) {
  console.log('Missing size');
} else {
  for (let v = 1; v < sqs; v++) {
    shape = shape + '#';
  }
  shape = shape.trim();

  for (let i = 0; i < sqs; i++) {
    console.log(shape);
  }
}
