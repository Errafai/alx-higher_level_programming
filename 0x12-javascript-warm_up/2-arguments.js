#!/usr/bin/node
const args = process.argv;

if (args.length === 3) {
  console.log('Argument found');
} else if (args.lenght > 3) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}
