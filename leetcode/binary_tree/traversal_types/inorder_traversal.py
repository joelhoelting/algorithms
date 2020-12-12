"""
Inorder Traversal

Left - Node - Right

       F
     /   \
    B     G
   / \     \
  A   D     I
     / \   /
    C   E H

Result: A-B-C-D-E-F-G-H-I
"""


# Recursive

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.dfs(root, res)
        return res

        def dfs(self, node, array):
            if node:
                self.dfs(node.left, res)
                res.append(node.val)
                self.dfs(node.right, res)
