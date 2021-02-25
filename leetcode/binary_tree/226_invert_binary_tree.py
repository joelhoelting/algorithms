from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# def invertTree(self, root: TreeNode) -> TreeNode:
#     if root is None:
#         return None

#     queue = deque([root])
#     while queue:
#         node = queue.popleft()
#         temp_left = node.left
#         node.left = node.right
#         node.right = temp_left
#         if node.left:
#             queue.append(node.left)
#         if node.right:
#             queue.append(node.right)

#     return root

def invertTree(self, root: TreeNode) -> TreeNode:
    if root is None:
        return None

    root.right = self.invertTree(root.right)
    root.left = self.invertTree(root.left)
    root.left = root.right
    root.right = root.left
    return root
