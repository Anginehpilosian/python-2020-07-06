/*
  String: Is Palindrome
  Create a function that returns a boolean whether the string is a strict palindrome.
    - palindrome = string that is same forwards and backwards

  Do not ignore spaces, punctuation and capitalization
 */

const test1 = "a x a";
// Output: true

const test2 = "racecar";
// Output: true

const test3 = "Dud";
// Output: false

const test4 = "oho!";
// Output: false

const sadiesFavoriteTestCase = "tacocat";
// Output: true


// Ninja Sensei Bonus / Further Study!

/*
  Longest Palindrome
  For this challenge, we will look not only at the entire string provided, but also at the substrings within it. Return the longest palindromic substring.
  Strings longer or shorter than complete words are OK.
  All the substrings of "abc" are:
  a, ab, abc, b, bc, c
*/

const test01 = "what up, daddy-o?";
// Output: "dad"

const test02 = "uh, not much";
// Output: "u"

const test03 = "Yikes! my favorite racecar erupted!";
// Output: "e racecar e"