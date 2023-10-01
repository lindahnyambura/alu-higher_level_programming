#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log(0); // Added semicolon
} else {
  const args = process.argv.map(Number)
    .slice(2, process.argv.length)
    .sort((a, b) => a - b);
  console.log(args[args.length - 2]); // Added semicolon
}
