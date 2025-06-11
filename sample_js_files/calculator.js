// calculator.js
// A class with methods and branching
// This Calculator class provides basic arithmetic operations and utility methods.
// It is designed for demonstration and code complexity analysis purposes.

class Calculator {
  constructor() {
    // Initialize the calculator value to zero
    this.value = 0;
  }

  // Add a number to the current value
  add(x) {
    this.value += x;
  }

  // Subtract a number from the current value
  subtract(x) {
    this.value -= x;
  }

  // Multiply the current value by a number
  multiply(x) {
    this.value *= x;
  }

  // Divide the current value by a number (throws on division by zero)
  divide(x) {
    if (x === 0) throw new Error('Division by zero');
    this.value /= x;
  }

  // Reset the calculator value to zero
  reset() {
    this.value = 0;
  }

  // Compute a single operation based on the op string
  compute(op, x) {
    if (op === 'add') {
      this.add(x);
    } else if (op === 'subtract') {
      this.subtract(x);
    } else {
      throw new Error('Unknown operation');
    }
    return this.value;
  }

  // Perform a sequence of operations from an array of {op, val} objects
  bulkOperations(arr) {
    for (let i = 0; i < arr.length; i++) {
      switch (arr[i].op) {
        case 'add':
          this.add(arr[i].val);
          break;
        case 'subtract':
          this.subtract(arr[i].val);
          break;
        case 'multiply':
          this.multiply(arr[i].val);
          break;
        case 'divide':
          this.divide(arr[i].val);
          break;
        default:
          break;
      }
    }
  }

  // Dummy methods for code padding and complexity demonstration
  method1() { return 1; }
  method2() { return 2; }
  method3() { return 3; }
  method4() { return 4; }
  method5() { return 5; }
  method6() { return 6; }
  method7() { return 7; }
  method8() { return 8; }
  method9() { return 9; }
  method10() { return 10; }
  method11() { return 11; }
  method12() { return 12; }
  method13() { return 13; }
  method14() { return 14; }
  method15() { return 15; }
  method16() { return 16; }
  method17() { return 17; }
  method18() { return 18; }
  method19() { return 19; }
  method20() { return 20; }
}

// Export the Calculator class for use in other modules
module.exports = Calculator;
