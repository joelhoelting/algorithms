"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its bottom-up level order traversal as:

[
  [15,7],
  [9,20],
  [3]
]

"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# BFS - Queue using deque

# from collections import deque
#
#
# class Solution:
#     def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
#         if root is None:
#             return None
#
#         queue = deque([root])
#         result = []
#
#         while queue:
#             num_of_nodes = len(queue)
#             current_row = []
#
#             while num_of_nodes > 0:
#                 current_node = queue.pop()
#                 current_row.append(current_node.val)
#
#                 if current_node.left:
#                     queue.appendleft(current_node.left)
#
#                 if current_node.right:
#                     queue.appendleft(current_node.right)
#
#                 num_of_nodes -= 1
#
#             result.append(current_row)
#
#         return result[::-1]

# BFS - Queue
# class Solution:
#     def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
#         stack = [root]  # It captures the root node at the very beginning.
#         levelOutput = []  # It captures the node values that are at the same level.
#         output = []  # End result
#         if root is None:  # If the root is empty, return None.
#             return (None)
#         while stack:
#             slen = len(stack)
#             while slen > 0:  # Keep traversing at the same level.
#                 temp = stack.pop(0)
#                 levelOutput.append(temp.val)
#                 if temp.left != None:
#                     stack.append(temp.left)
#                 if temp.right != None:
#                     stack.append(temp.right)
#                 slen -= 1
#             output.append(levelOutput.copy())
#             levelOutput.clear()
#         return (output[::-1])  # Reverse the 2D list.

# BFS - Recursive
# BFS - Queue using deque

# from collections import deque
#
#
# class Solution:
#     def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
#         if root is None:
#             return None
#
#         queue = deque([root])
#         result = []
#
#         while queue:
#             num_of_nodes = len(queue)
#             current_row = []
#
#             while num_of_nodes > 0:
#                 current_node = queue.pop()
#                 current_row.append(current_node.val)
#
#                 if current_node.left:
#                     queue.appendleft(current_node.left)
#
#                 if current_node.right:
#                     queue.appendleft(current_node.right)
#
#                 num_of_nodes -= 1
#
#             result.append(current_row)
#
#         return result[::-1]

# BFS - Queue
# class Solution:
#     def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
#         stack = [root]  # It captures the root node at the very beginning.
#         levelOutput = []  # It captures the node values that are at the same level.
#         output = []  # End result
#         if root is None:  # If the root is empty, return None.
#             return (None)
#         while stack:
#             slen = len(stack)
#             while slen > 0:  # Keep traversing at the same level.
#                 temp = stack.pop(0)
#                 levelOutput.append(temp.val)
#                 if temp.left != None:
#                     stack.append(temp.left)
#                 if temp.right != None:
#                     stack.append(temp.right)
#                 slen -= 1
#             output.append(levelOutput.copy())
#             levelOutput.clear()
#         return (output[::-1])  # Reverse the 2D list.

# BFS - Recursive
# BFS - Queue using deque

# from collections import deque
#
#
# class Solution:
#     def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
#         if root is None:
#             return None
#
#         queue = deque([root])
#         result = []
#
#         while queue:
#             num_of_nodes = len(queue)
#             current_row = []
#
#             while num_of_nodes > 0:
#                 current_node = queue.pop()
#                 current_row.append(current_node.val)
#
#                 if current_node.left:
#                     queue.appendleft(current_node.left)
#
#                 if current_node.right:
#                     queue.appendleft(current_node.right)
#
#                 num_of_nodes -= 1
#
#             result.append(current_row)
#
#         return result[::-1]

# BFS - Queue
# class Solution:
#     def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
#         stack = [root]  # It captures the root node at the very beginning.
#         levelOutput = []  # It captures the node values that are at the same level.
#         output = []  # End result
#         if root is None:  # If the root is empty, return None.
#             return (None)
#         while stack:
#             slen = len(stack)
#             while slen > 0:  # Keep traversing at the same level.
#                 temp = stack.pop(0)
#                 levelOutput.append(temp.val)
#                 if temp.left != None:
#                     stack.append(temp.left)
#                 if temp.right != None:
#                     stack.append(temp.right)
#                 slen -= 1
#             output.append(levelOutput.copy())
#             levelOutput.clear()
#         return (output[::-1])  # Reverse the 2D list.

# BFS - Recursive
# BFS - Queue using deque

# from collections import deque
#
#
# class Solution:
#     def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
#         if root is None:
#             return None
#
#         queue = deque([root])
#         result = []
#
#         while queue:
#             num_of_nodes = len(queue)
#             current_row = []
#
#             while num_of_nodes > 0:
#                 current_node = queue.pop()
#                 current_row.append(current_node.val)
#
#                 if current_node.left:
#                     queue.appendleft(current_node.left)
#
#                 if current_node.right:
#                     queue.appendleft(current_node.right)
#
#                 num_of_nodes -= 1
#
#             result.append(current_row)
#
#         return result[::-1]

# BFS - Queue
# class Solution:
#     def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
#         stack = [root]  # It captures the root node at the very beginning.
#         levelOutput = []  # It captures the node values that are at the same level.
#         output = []  # End result
#         if root is None:  # If the root is empty, return None.
#             return (None)
#         while stack:
#             slen = len(stack)
#             while slen > 0:  # Keep traversing at the same level.
#                 temp = stack.pop(0)
#                 levelOutput.append(temp.val)
#                 if temp.left != None:
#                     stack.append(temp.left)
#                 if temp.right != None:
#                     stack.append(temp.right)
#                 slen -= 1
#             output.append(levelOutput.copy())
#             levelOutput.clear()
#         return (output[::-1])  # Reverse the 2D list.

# BFS - Recursive
# BFS - Queue using deque

# from collections import deque
#
#
# class Solution:
#     def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
#         if root is None:
#             return None
#
#         queue = deque([root])
#         result = []
#
#         while queue:
#             num_of_nodes = len(queue)
#             current_row = []
#
#             while num_of_nodes > 0:
#                 current_node = queue.pop()
#                 current_row.append(current_node.val)
#
#                 if current_node.left:
#                     queue.appendleft(current_node.left)
#
#                 if current_node.right:
#                     queue.appendleft(current_node.right)
#
#                 num_of_nodes -= 1
#
#             result.append(current_row)
#
#         return result[::-1]

# BFS - Queue
# class Solution:
#     def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
#         stack = [root]  # It captures the root node at the very beginning.
#         levelOutput = []  # It captures the node values that are at the same level.
#         output = []  # End result
#         if root is None:  # If the root is empty, return None.
#             return (None)
#         while stack:
#             slen = len(stack)
#             while slen > 0:  # Keep traversing at the same level.
#                 temp = stack.pop(0)
#                 levelOutput.append(temp.val)
#                 if temp.left != None:
#                     stack.append(temp.left)
#                 if temp.right != None:
#                     stack.append(temp.right)
#                 slen -= 1
#             output.append(levelOutput.copy())
#             levelOutput.clear()
#         return (output[::-1])  # Reverse the 2D list.

# BFS - Recursive
# BFS - Queue using deque

# from collections import deque
#
#
# class Solution:
#     def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
#         if root is None:
#             return None
#
#         queue = deque([root])
#         result = []
#
#         while queue:
#             num_of_nodes = len(queue)
#             current_row = []
#
#             while num_of_nodes > 0:
#                 current_node = queue.pop()
#                 current_row.append(current_node.val)
#
#                 if current_node.left:
#                     queue.appendleft(current_node.left)
#
#                 if current_node.right:
#                     queue.appendleft(current_node.right)
#
#                 num_of_nodes -= 1
#
#             result.append(current_row)
#
#         return result[::-1]

# BFS - Queue
# class Solution:
#     def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
#         stack = [root]  # It captures the root node at the very beginning.
#         levelOutput = []  # It captures the node values that are at the same level.
#         output = []  # End result
#         if root is None:  # If the root is empty, return None.
#             return (None)
#         while stack:
#             slen = len(stack)
#             while slen > 0:  # Keep traversing at the same level.
#                 temp = stack.pop(0)
#                 levelOutput.append(temp.val)
#                 if temp.left != None:
#                     stack.append(temp.left)
#                 if temp.right != None:
#                     stack.append(temp.right)
#                 slen -= 1
#             output.append(levelOutput.copy())
#             levelOutput.clear()
#         return (output[::-1])  # Reverse the 2D list.

# BFS - Recursive
def levelOrderBottom(self, root):
    if root is None:
        return []
    res = []
    self.dfs([root], res)
    return res


def dfs(self, level_nodes, res):
    if not level_nodes: return
    res.insert(0, [])
    temp = []
    for node in level_nodes:
        res[0].append(node.val)
        if node.left: temp.append(node.left)
        if node.right: temp.append(node.right)
    self.dfs(temp, res)
