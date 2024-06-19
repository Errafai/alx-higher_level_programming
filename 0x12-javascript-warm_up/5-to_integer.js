#!/usr/bin/node
if (typeof Number(process.argv[2]) === 'number') {
  console.log(Number(process.argv[2]));
} else {
  console.log('Not a number');
}
