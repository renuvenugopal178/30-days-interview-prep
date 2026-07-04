# Day 2 Notes: Arrays, Strings, Complexity, Sorting, Searching

## Time Complexity

| Complexity | Meaning | Example |
|---|---|---|
| O(1) | Constant work | Access `numbers[0]` |
| O(log n) | Repeatedly halves input | Binary search |
| O(n) | One full pass | Find maximum in an array |
| O(n log n) | Efficient comparison sorting | Merge sort, built-in sort |
| O(n²) | Nested loops over input | Compare every pair |

## Space Complexity
Extra memory used by an algorithm apart from the input.

- `O(1)`: only a few variables.
- `O(n)`: a dictionary, set, or new list proportional to input size.

## Important Rule
Nested loops do not always mean O(n²). If two pointers move across an array only once, the total can still be O(n).
## Linear Search
Checks each element one by one.
Time: O(n)
Space: O(1)

## Binary Search
Checks the middle element and discards half of the remaining range.
Requirement: input must be sorted.
Time: O(log n)
Space: O(1)