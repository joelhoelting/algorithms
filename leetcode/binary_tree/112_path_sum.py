class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

# Recursive
def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
  if not root:
      return False
  
  targetSum -= root.val
  
  if root.left == None and root.right == None:
      if targetSum == 0:
          return True
      return False
  
  return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)

# Iterative
def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
  if root is None:
      return False
  
  q = [(root, root.val)]
  
  while q:
      curr_node, curr_sum = q.pop(0)
      
      if curr_sum == targetSum and not curr_node.left and not curr_node.right:
          return True
      if curr_node.left:
          q.append((curr_node.left, curr_sum + curr_node.left.val))
      if curr_node.right:
          q.append((curr_node.right, curr_sum + curr_node.right.val))
  
  return False

