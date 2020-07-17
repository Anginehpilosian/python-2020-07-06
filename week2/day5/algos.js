/*
  Trim
  Given a string that may have extra spaces at the start and the end,
  return a new string that has the extra spaces at the start and the end trimmed (removed)
  do not remove any other spaces.
*/

const test1 = "   hello world     "
// Output: "hello world"

// ******************************************************************************

/*
  Given an array of objects / dictionaries to represent new inventory,
  and an array of objects / dictionarys to represent current inventory,
  update the quantities of the current inventory
  if the item doesn't exist in current inventory, add it to the inventory

  return the current inventory after updating it.
*/

const test1NewInv = [
  { name: "Grain of Rice", quantity: 9000 },
  { name: "Peanut Butter", quantity: 50 },
  { name: "Royal Jelly", quantity: 20 },
]
const test1CurrInv = [
  { name: "Peanut Butter", quantity: 20 },
  { name: "Grain of Rice", quantity: 1 },
]
/*
  Output: [
    { name: "Peanut Butter", quantity: 70 },
    { name: "Grain of Rice", quantity: 90001 },
    { name: "Royal Jelly", quantity: 20 },
  ]
 */

const test2NewInv = []
const test2CurrInv = [{ name: "Peanut Butter", quantity: 20 }]
// Output: [{ name: "Peanut Butter", quantity: 20 }]

const test3NewInv = [{ name: "Peanut Butter", quantity: 20 }]
const test3CurrInv = []
// Output: [{ name: "Peanut Butter", quantity: 20 }]

// ******************************************************************************

/*
  An anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
  typically using all the original letters exactly once.

  Is there a quick way to determine if they aren't an anagram before spending more time?

  Given two strings
  return whether or not they are anagrams
*/

const input1StrA = "yes"
const input1StrB = "eys"
// Output: true

const input2StrA = "yes"
const input2StrB = "eYs"
// Output: true

const input3StrA = "no"
const input3StrB = "noo"
// Output: false

const input4StrA = "silent"
const input4StrB = "listen"
// Output: true
