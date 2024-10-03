#!/usr/bin/node
const av = process.argv;

if (av.length <= 3) {
  console.log('0');
} else {
  let max1 = Number(av[2]);
  let max2 = Number(av[2]);
  for (const item of av.slice(3)) {
    if (max1 < Number(item)) {
      max1 = Number(item);
    }
    if (max2 < Number(item) && Number(item) !== max1) {
      max2 = Number(item);
    }
  }
  console.log(Number(max2));
}
