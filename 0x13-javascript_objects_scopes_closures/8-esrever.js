#!/usr/bin/node

exports.esrever = function (list) {
  const esrevered = [];

  for (let i = list.length - 1; i >= 0; i--) {
    esrevered.push(list[i]);
  }
  return esrevered;
};
