"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

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


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Depth First Search
def min_depth(self, root: TreeNode) -> int:
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return 1

    left_depth = self.minDepth(root.left) if root.left else float('inf')
    right_depth = self.minDepth(root.right) if root.right else float('inf')

    return 1 + min(left_depth, right_depth)


# Breadth First Search
def min_depth(self, root: TreeNode) -> int:
    if root is None:
        return 0

    queue = list()
    queue.append(root)

    depth = 0
    while queue:
        num_of_nodes = len(queue)

        while num_of_nodes > 0:
            current_node = queue.pop(0)

            if not current_node.left and not current_node.right:
                return depth + 1

            if current_node.left:
                queue.append(current_node.left)

            if current_node.right:
                queue.append(current_node.right)

            num_of_nodes -= 1

        depth += 1
