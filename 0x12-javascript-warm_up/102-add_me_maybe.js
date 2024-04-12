#!/usr/bin/node
function incrementAndCall (number, theFunction) {
  const incremented = number + 1;
  theFunction(incremented);
}
module.exports = incrementAndCall;
