"""
You are given a binary tree.
Write a function that can return the inorder traversal of node values.
Example:
Input:
   3
    \
     1
    /
   5
Output: [3,5,1]
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""recursive solution"""
def inorder_traversal(root):
    # create an inner helper function
    def helper(root, result):
        # if root exists
        if root:
            # caller helper on left of root, passing the result list along
            helper(root.left, result)
            # inorder thing!
            # append roots value to the result list
            result.append(root.val)
            # call the helper on the right of the root, pass the result list along
            helper(root.right, result)

    result = []
    helper(root, result)

    return result        


t1 = TreeNode(3)
t1.right = TreeNode(1)
t1.right.left = TreeNode(5)

print(inorder_traversal(t1))