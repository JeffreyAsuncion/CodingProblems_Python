"""
You are given a binary tree. You need to write a function that can determin if
it is a valid binary search tree.
The rules for a valid binary search tree are:
- The node's left subtree only contains nodes with values less than the node's
value.
- The node's right subtree only contains nodes with values greater than the
node's value.
- Both the left and right subtrees must also be valid binary search trees.
Example 1:
Input:
    5
   / \
  3   7
Output: True

Example 2:
Input:
    10
   / \
  2   8
     / \
    6  12
Output: False
Explanation: The root node's value is 10 but its right child's value is 8.
"""
import math # to get the lower and upper bounds math.inf
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    """recursive solution"""
    def is_valid_BST_recursive(self, root):

        # default True as the result as BST
        valid = True

        # if left child exists
        if root.left:
            # check if the left child is smaller that the root node
            valid = valid and root.left.value < root.value
            # check not valid
            if not valid:
                # return not valid
                return False

            valid = valid and self.is_valid_BST_recursive(root.left)

        # if right child exists
        if root.right:
            # check that the right child is larger that the root node
            valid = valid and root.right.value > root.value
            # check not valid
            if not valid:
                # return not valid
                return False

            valid = valid and self.is_valid_BST_recursive(root.right)
            
        # return result
        return valid


    

b1 = TreeNode(5)
b1.left = TreeNode(3)
b1.right = TreeNode(7)

b2 = TreeNode(10)
b2.left = TreeNode(2)
b2.right = TreeNode(8)
b2.right.left = TreeNode(6)
b2.right.right = TreeNode(12)



print(b1.is_valid_BST_recursive(b1)) # True
print(b2.is_valid_BST_recursive(b2)) # False