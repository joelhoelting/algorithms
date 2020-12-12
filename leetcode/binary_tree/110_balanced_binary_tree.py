"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

    a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

     1
   /   \
  2     2
       / \
      4   3

output: 2

    1
  /   \
 2     2
  \     \
   3     3

output: 3
"""


def isBalanced(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if not root:
        return True
    if self.depth(root) == -1:
        return False
    else:
        return True


def depth(self, root):
    if not root:
        return 0

    left = self.depth(root.left)
    right = self.depth(root.right)

    if abs(left - right) > 1 or left == -1 or \
            right == -1:
        return -1
    return max(left, right) + 1
