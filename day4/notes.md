# Day 4 Notes

## Binary Tree
A structure where each node has at most two children: left and right.

## Binary Search Tree
For every node:
- left subtree values are smaller
- right subtree values are larger

## Traversal
- Inorder: Left → Root → Right
- Preorder: Root → Left → Right
- Postorder: Left → Right → Root

## Complexity
For a balanced BST:
- Search: O(log n)
- Insert: O(log n)

For an unbalanced BST:
- Search: O(n)
- Insert: O(n)

## Recursion in Trees
Base case: if node is None, return.
Recursive case: process children.