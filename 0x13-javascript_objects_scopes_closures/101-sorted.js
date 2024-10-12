#!/usr/bin/node

const dict = require('./101-data.js').dict;
const ds = {};
for (const value of Object.values(dict)) {
  ds[value] = [];
  for (const key of Object.keys(dict)) {
    if (dict[key] === value) {
      ds[value].push(key);
    } 
  }
}
console.log(ds);
