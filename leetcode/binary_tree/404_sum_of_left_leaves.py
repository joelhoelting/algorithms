class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sumOfLeftLeaves(self, root: TreeNode) -> int:
  if not root:
      return 0
  
  if root.left and not root.left.left and not root.left.right:
      return root.left.val + self.sumOfLeftLeaves(root.right)
  else:
      return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)


def sumOfLeftLeaves(self, root: TreeNode) -> int:
  if not root or (root.left is None and root.right is None):
      return 0
  
  res, stack = 0, [root]
  
  while stack:
    node = stack.pop()
    if node.left:
      if node.left.left is None and node.left.right is None:
        res += node.left.val
      else:
        stack.append(node.left)
    if node.right:
      stack.append(node.right)
  
  return res