/*
  Join
  Given an arr and a separator string, output a string of every item in the array separated by the separator.

  No trailing separator at the end
  Default the separator to a comma with a space after it if no separator is provided
*/

const test1Arr = [1, 2, 3]
const test1Separator = ", "
// Output: "1, 2, 3";

const test2Arr = [1, 2, 3]
const test2Separator = "-"
// Output: "1-2-3";

const test3Arr = [1, 2, 3]
const test3Separator = " - "
// Output: "1 - 2 - 3";

const test4Arr = [1]
const test4Separator = ", "
// Output: "1";

const test5Arr = []
const test5Separator = ", "
// Output: "";

// ********************************************

/*
  Book Index

  Given an arry of ints representing page numbers
  return a string with the page numbers formatted as page ranges when the nums span a consecutive range
*/

const test1 = [1, 13, 14, 15, 37, 38, 70]
// Output: "1, 13-15, 37-38, 70"
