#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let nb = 0;
  for (const i of list) {
    if (i === searchElement) {
      nb++;
    }
  }
  return nb;
};
