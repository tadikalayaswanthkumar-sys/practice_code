// Read numbers passed from terminal arguments (e.g. node add.js 10 20)
let args = process.argv.slice(2);
let firstnumber = Number(args[0]);
let secondnumber = Number(args[1]);
let sum = firstnumber + secondnumber;
console.log(sum);

