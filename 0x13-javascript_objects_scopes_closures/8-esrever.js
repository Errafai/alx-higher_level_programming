#!/usr/bin/node

exports.esrever = function (list) {
  let i = 0;
  let j = list.length - 1;
  const list2 = list.slice(0, 4);
  for (; i < j; j--, i++) {
    list2[i] = list[j];
    list2[j] = list[i];
  }
  return list;
};
