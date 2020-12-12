"""
Preorder Traversal

Node - Left - Right

       F
     /   \
    B     G
   / \     \
  A   D     I
     / \   /
    C   E H

Result: F-B-A-D-C-E-G-I-H
"""


# Recursive

def preorder_traversal(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    res = []
    self.dfs(root, res)
    return res


def dfs(self, node, array):
    if root:
        res.append(root.val)
        self.dfs(root.left, res)
        self.dfs(root.right, res)

# Iterative

# def preorder_traversal(self, root)
#     stack, res = [root], []
#
#     while stack:
#         curr_node = stack.pop()
#         if curr_node:
#             res.append(curr_node.val)
#             stack.append(curr_node.right)
#             stack.append(curr_node.left)
#
#     return res
