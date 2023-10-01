#!/usr/bin/node

function add(a, b) {
  return a + b;  // Added semicolon
}

console.log(add(Number(process.argv[2]), Number(process.argv[3])));  // Added semicolon
