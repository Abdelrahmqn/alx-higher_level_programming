#!/usr/bin/node
function callMeMoby (x, theFunction) {
  for (let i = 1; i <= x; i++) {
    theFunction();
  }
}
module.exports.callMeMoby = callMeMoby;
