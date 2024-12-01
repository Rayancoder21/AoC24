# Advent of Code 2024 - Day 1: Historian Hysteria

The Chief Historian is always present for the big Christmas sleigh launch, but nobody has seen him in months! Last anyone heard, he was visiting locations that are historically significant to the North Pole; a group of Senior Historians has asked you to accompany them as they check the places they think he was most likely to visit.

As each location is checked, they will mark it on their list with a star. They figure the Chief Historian must be in one of the first fifty places they'll look, so in order to save Christmas, you need to help them get fifty stars on their list before Santa takes off on December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

---

## Problem Description

You haven't even left yet, and the group of Elvish Senior Historians has already hit a problem: their list of locations to check is currently empty. Eventually, someone decides that the best place to check first would be the Chief Historian's office.

Upon pouring into the office, everyone confirms that the Chief Historian is indeed nowhere to be found. Instead, the Elves discover an assortment of notes and lists of historically significant locations! This seems to be the planning the Chief Historian was doing before he left. Perhaps these notes can be used to determine which locations to search?

Throughout the Chief's office, the historically significant locations are listed not by name but by a unique number called the location ID. To make sure they don't miss anything, The Historians split into two groups, each searching the office and trying to create their own complete list of location IDs.

There's just one problem: by holding the two lists up side by side (your puzzle input), it quickly becomes clear that the lists aren't very similar. Maybe you can help The Historians reconcile their lists?

---

### Example Input:
**first coulmn:**
3 4 2 1 3 3
**second column:**
4 3 5 3 9 3

---

### Part One(the code is in task1.py):

To find out how far apart the two lists are:

1. Pair up the smallest number in the left list with the smallest number in the right list, then the second-smallest left number with the second-smallest right number, and so on.
2. Within each pair, figure out how far apart the two numbers are by calculating the absolute difference.
3. Sum up all the distances.

For example:

- Pairing the smallest numbers: `1` (left) and `3` (right) → distance = `2`.
- Second smallest: `2` and `3` → distance = `1`.
- Next: `3` and `3` → distance = `0`.
- And so on...

The total distance for the example input is:
2 + 1 + 0 + 1 + 2 + 5 = 11

**Your Puzzle Answer should be: 2375403**

---

### Part Two(the code is in task2.py):

This time, instead of distances, calculate a **similarity score**:

1. For each number in the left list, count how many times it appears in the right list.
2. Multiply the number by its frequency and add it to the total similarity score.

For example, using the same input:

- `3` appears `3` times in the right list → `3 * 3 = 9`.
- `4` appears `1` time in the right list → `4 * 1 = 4`.
- `2` and `1` do not appear in the right list → `0`.
- Repeat for all numbers.

The total similarity score for the example is:
9 + 4 + 0 + 0 + 9 + 9 = 31


**Your Puzzle Answer should be: 23082277**

---

## Completion Status

Both parts of this puzzle are complete! 🎉

---

## Notes

- Each part provides one gold star (`**`).
