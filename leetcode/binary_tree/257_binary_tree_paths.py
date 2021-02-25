"""
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Stack
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root: return []
        stack = [(root,str(root.val))]
        res = []
        while stack:
            node, path = stack.pop()
            if node.left:
                stack.append((node.left, path+"->"+str(node.left.val)))
            if node.right:
                stack.append((node.right, path+"->"+str(node.right.val)))
            if not node.left and not node.right:
                res.append(path)
        return res

# Recursion
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> 'List'[str]:
        res = []
        def dfs(node, array):
            if node:
                array.append(str(node.val))
                if not node.left and not node.right:
                    res.append('->'.join(array))
                else:
                    dfs(node.left, array)
                    dfs(node.right, array)
                array.pop()
        dfs(root, [])
        return res

