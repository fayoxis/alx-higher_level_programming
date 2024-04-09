#!/usr/bin/node
// Import the Square module
const Square = require('./6-square');

// Create a new instance of Square with size 4
const s1 = new Square(4);

// Call the charPrint method without passing any argument
s1.charPrint();

// Call the charPrint method and pass 'C' as the character argument
s1.charPrint('C');

// The output will remain the same as before.
