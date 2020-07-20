/*
  Balance Index

  Here, a balance point is ON an index, not between indices.

  Return the balance index where sums are equal on either side
  (exclude its own value).

  Return -1 if none exist.
*/

const test1 = [-2, 5, 7, 0, 3]
// Output: 2

const test2 = [9, 9]
// Output: -1

// *****************************************************************************

/*
  Balance Point

  Write a function that returns whether the given
  array has a balance point BETWEEN indices,
  where one side’s sum is equal to the other’s.
*/

const test1 = [1, 2, 3, 4, 10]
// Output: true (between indices 3 & 4)

const test2 = [1, 2, 4, 2, 1]
//  Output: false
