#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const args = process.argv.slice(2)
    .map(Number)
    .sort((a, b) => a - b);
  console.log(args[args.length - 2]);
}
