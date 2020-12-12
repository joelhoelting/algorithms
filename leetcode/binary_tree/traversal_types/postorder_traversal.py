"""
Inorder Traversal

Left - Right - Node

       F
     /   \
    B     G
   / \     \
  A   D     I
     / \   /
    C   E H

Result: A-C-E-D-B-H-I-G-F
"""


# Recursive

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.dfs(root, res)
        return res

    def dfs(self, node, array):
        if root:
            self.dfs(root.left, res)
            self.dfs(root.right, res)
            res.append(root.val)
