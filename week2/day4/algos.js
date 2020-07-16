/*
  String: Rotate String

  Create a standalone function that accepts a string and an integer, and rotates the characters in the string to the right by that given integer amount.
*/

const test1Str = "Hello World"
const test1RotateAmnt = 0
// Output: "Hello World"

const test1Str = "Hello World"
const test1RotateAmnt = 1
// Output: "dHello Worl"

const test1Str = "Hello World"
const test1RotateAmnt = 2
// Output: "ldHello Wor"

const test1Str = "Hello World"
const test1RotateAmnt = 4
// Output: "orldHello W"

// **************************

/*
  String: ionIs Rotat (Is Rotation)

  Create the function isRotation(str1,str2) that
  returns whether the second string is a rotation of the first.
*/

const test1StrA = "ABCD"
const test1StrB = "CDAB"
// Output: true
//   - if you start from A in the 2nd string, the letters are in the same order, just rotated

const test2StrA = "ABCD"
const test2StrB = "CDBA"
// Output: false
//   - all same letters in 2nd string, but out of order
