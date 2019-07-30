"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

"""


from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        left = self.valid_bst(root.left, None, root.val)
        right = self.valid_bst(root.right, root.val, None)
        return left and right
    
    def valid_bst(self, root: TreeNode, lower: int, upper: int) -> bool:
        if not root:
            return True
        valid = True
        if lower != None and root.val <= lower:
            valid = False
        if upper != None and root.val >= upper:
            valid = False
        if root.left:
            valid = valid and self.valid_bst(root.left, lower, root.val)
        if root.right:
            valid = valid and self.valid_bst(root.right, root.val, upper)
        return valid


