// complex.js
// This file contains more complex functions with nested logic and branching for demonstration.

/**
 * Process an array with nested logic and return a computed result
 * @param {Array} arr - The input array
 * @returns {number} - The computed result
 */
function processData(arr) {
  let result = 0;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] % 2 === 0) {
      // Double even numbers
      result += arr[i] * 2;
    } else {
      // For odd numbers, sum up to their value
      for (let j = 0; j < arr[i]; j++) {
        result += j;
      }
    }
  }
  return result;
}

/**
 * Deeply nested loops for complexity demonstration
 * @param {number} n - The depth of nesting
 * @returns {number} - The computed result from nested loops
 */
function deepNest(n) {
  let x = 0;
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      for (let k = 0; k < n; k++) {
        x += i + j + k;
      }
    }
  }
  return x;
}

/**
 * Function with many branches for complexity
 * @param {number} x - The input number
 * @returns {number} - The branch result
 */
function lotsOfBranches(x) {
  if (x < 10) return 1;
  else if (x < 20) return 2;
  else if (x < 30) return 3;
  else if (x < 40) return 4;
  else if (x < 50) return 5;
  else if (x < 60) return 6;
  else if (x < 70) return 7;
  else if (x < 80) return 8;
  else if (x < 90) return 9;
  else return 10;
}

// Add more dummy functions to reach ~200 lines

/**
 * Dummy function that returns true
 * @returns {boolean} - Always returns true
 */
function dummyFunction1() {
  return true;
}

/**
 * Dummy function that returns false
 * @returns {boolean} - Always returns false
 */
function dummyFunction2() {
  return false;
}

/**
 * Dummy function that adds two numbers
 * @returns {number} - The sum of two numbers
 */
function dummyFunction3() {
  let a = 1;
  let b = 2;
  return a + b;
}

/**
 * Dummy function that returns the length of a string
 * @returns {number} - The length of the string "Hello, World!"
 */
function dummyFunction4() {
  let str = "Hello, World!";
  return str.length;
}

/**
 * Dummy function that sums an array of numbers
 * @returns {number} - The sum of the array [1, 2, 3, 4, 5]
 */
function dummyFunction5() {
  let arr = [1, 2, 3, 4, 5];
  return arr.reduce((acc, val) => acc + val, 0);
}

/**
 * Dummy function that counts the keys in an object
 * @returns {number} - The number of keys in the object { a: 1, b: 2, c: 3 }
 */
function dummyFunction6() {
  let obj = { a: 1, b: 2, c: 3 };
  return Object.keys(obj).length;
}

/**
 * Dummy function that returns the size of a set
 * @returns {number} - The size of the set new Set([1, 2, 2, 3, 4])
 */
function dummyFunction7() {
  let set = new Set([1, 2, 2, 3, 4]);
  return set.size;
}

/**
 * Dummy function that gets a value from a map by key
 * @returns {number} - The value associated with the key "b" in the map
 */
function dummyFunction8() {
  let map = new Map();
  map.set("a", 1);
  map.set("b", 2);
  map.set("c", 3);
  return map.get("b");
}

/**
 * Dummy function that checks if a weak set has a value
 * @returns {boolean} - Whether the weak set has the object as a member
 */
function dummyFunction9() {
  let weakSet = new WeakSet();
  let obj = {};
  weakSet.add(obj);
  return weakSet.has(obj);
}

/**
 * Dummy function that gets a value from a weak map by key
 * @returns {string} - The value associated with the object key in the weak map
 */
function dummyFunction10() {
  let weakMap = new WeakMap();
  let obj = {};
  weakMap.set(obj, "value");
  return weakMap.get(obj);
}

// Export all functions as an object
module.exports = { processData, deepNest, lotsOfBranches };
