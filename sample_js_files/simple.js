// simple.js
// This file contains a collection of simple arithmetic functions for demonstration.
// Each function performs a basic operation and is exported for use in other modules.

// Add two numbers
function add(a, b) { return a + b; }
// Subtract b from a
function subtract(a, b) { return a - b; }
// Multiply two numbers
function multiply(a, b) { return a * b; }
// Divide a by b (returns 0 if b is zero)
function divide(a, b) { return b !== 0 ? a / b : 0; }
// Modulo operation
function mod(a, b) { return a % b; }
// Exponentiation
function pow(a, b) { return Math.pow(a, b); }
// Increment a by 1
function inc(a) { return a + 1; }
// Decrement a by 1
function dec(a) { return a - 1; }
// Double the value
function double(a) { return a * 2; }
// Triple the value
function triple(a) { return a * 3; }
// Square the value
function square(a) { return a * a; }
// Cube the value
function cube(a) { return a * a * a; }
// Negate the value
function negate(a) { return -a; }
// Absolute value
function abs(a) { return Math.abs(a); }
// Maximum of two numbers
function max(a, b) { return Math.max(a, b); }
// Minimum of two numbers
function min(a, b) { return Math.min(a, b); }
// Average of two numbers
function avg(a, b) { return (a + b) / 2; }
// Sum all elements in an array
function sum(arr) { return arr.reduce((a, b) => a + b, 0); }
// Product of all elements in an array
function product(arr) { return arr.reduce((a, b) => a * b, 1); }
// No operation (dummy function)
function noop() { return; }

// ...repeat similar dummy functions to reach ~200 lines

// Export all functions as an object
module.exports = { add, subtract, multiply, divide, mod, pow, inc, dec, double, triple, square, cube, negate, abs, max, min, avg, sum, product, noop };
