#!/usr/bin/node
const args = process.argv;

if (args.length === 3) {
  console.log('Argument found');
} else if (args.length >= 4) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}
