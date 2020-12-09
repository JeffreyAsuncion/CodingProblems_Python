"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # node is None -> base case
        if root is None:
            return 0
        else:
            # otherwise root is not None
            # 1 is for the root node
            # call the recusive fn on right and left
            return 1 + max (
                self.maxDepth(root.left),
                self.maxDepth(root.right)
            )
