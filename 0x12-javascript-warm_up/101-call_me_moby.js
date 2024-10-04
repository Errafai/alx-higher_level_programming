#!/usr/bin/node
exports.callMeMoby = function callMeMoby (x, theFunction) {
  while (x--) {
    theFunction();
  }
};
