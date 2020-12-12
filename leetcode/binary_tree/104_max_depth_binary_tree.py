"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path
from the root node down to the farthest leaf node.

     1
   /   \
  2     2
       / \
      4   3

output: 3


    1
  /   \
 2     2
  \     \
   3     3

output: 3
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root: TreeNode) -> int:
    if not root:
        return 0

    left = self.maxDepth(root.left)
    right = self.maxDepth(root.right)
    return max(left, right) + 1
