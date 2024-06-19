#!/usr/bin/node
const argv = process.argv;
if (Number(argv[2])) {
  for (let i = 0; i < parseInt(argv[2]); i++) {
    let line = '';
    for (let j = 0; j < parseInt(argv[2]); j++) {
      line += 'x';
    }
    console.log(line);
  }
} else {
  console.log('Missing size');
}
