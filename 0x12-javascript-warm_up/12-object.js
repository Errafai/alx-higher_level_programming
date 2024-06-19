#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
Object.defineProperty(myObject, 'value', {
  configurable: true,
  value: 89
});
console.log(myObject);
