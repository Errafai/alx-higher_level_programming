#!/usr/bin/node

function fact (N) {
  if (N === 1 || N === 0 || isNaN(N)) {
    return 1;
  }
  return N * fact(N - 1);
}

console.log(fact(parseInt(process.argv[2])));
