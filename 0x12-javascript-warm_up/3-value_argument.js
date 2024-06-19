#!/usr/bin/node
const { argv } = require('node:process');

if (argv[2] === undefined) {
  console.log('No Argument');
} else {
  console.log(argv[2]);
}
