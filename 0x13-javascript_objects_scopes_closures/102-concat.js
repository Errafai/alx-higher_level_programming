#!/usr/bin/node

const ar = process.argv.slice(2);
const fs = require('fs');

const file1 = fs.readFileSync(ar[0], 'utf8');

const file2 = fs.readFileSync(ar[1], 'utf8');

fs.writeFileSync(ar[2], file1 + file2, 'utf8');
