#!/usr/bin/node
const av = process.argv;

if (av.length <= 3) {
  console.log('0');
} else {
  let min = Number(av[2]);
  for (const item of av.slice(3)) {
    if (min > Number(item)) {
      min = Number(item);
    }
  }
  console.log(min);
}
