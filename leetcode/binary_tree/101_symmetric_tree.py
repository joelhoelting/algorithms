"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1, 2, 2, 3, 4, 4, 3] is symmetric:

     1
   /   \
  2     2
 / \   / \
3   4 4   3

output: true

But the following [1, 2, 2, null, 3, null, 3] is not:

    1
  /   \
 2     2
  \      \
   3      3

output: false
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recursive
# def isSymmetric(self, root: TreeNode) -> bool:
#     if not root:
#         return True
#
#     def isMirror(node1, node2):
#         if not node1 or not node2:
#             return node1 == node2
#         if node1.val != node2.val:
#             return False
#         return isMirror(node1.left, node2.right) and isMirror(node1.right, node2.left)
#
#     return isMirror(root.left, root.right)


# Stack
def isSymmetric(self, root: TreeNode) -> bool:
    if root is None:
        return True
    stack = [(root, root)]

    while stack:
        node1, node2 = stack.pop()
        if node1 is None and node2 is None:
            pass
        elif node1 is None or node2 is None:
            return False
        elif node1.val != node2.val:
            return False
        else:
            stack.append((node1.left, node2.right))
            stack.append((node1.right, node2.left))

    return True
