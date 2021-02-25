"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

    6
   / \
  2  8
    / \
   7   9

Input: root = [6,2,8,null,null,7,9,null,null,null,null], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

"""

# Iterative (no stack or queue)


def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    parent_val = root.val

    p_val = p.val
    q_val = q.val

    if p_val > parent_val and q_val > parent_val:
        return self.lowestCommonAncestor(root.right, p, q)
    elif p_val < parent_val and q_val < parent_val:
        return self.lowestCommonAncestor(root.left, p, q)
    else:
        return root

# Recursive


def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    parent_val = root.val

    p_val = p.val
    q_val = q.val

    if p_val > parent_val and q_val > parent_val:
        return self.lowestCommonAncestor(root.right, p, q)
    elif p_val < parent_val and q_val < parent_val:
        return self.lowestCommonAncestor(root.left, p, q)
    else:
        return root
