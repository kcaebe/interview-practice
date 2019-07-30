"""
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]

"""


from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def inorderTraversal(self, root: 'TreeNode') -> List[int]:
        if root == None:
            return []
        stack, trav, visited = [], [], set()
        stack.append(root)
        while len(stack) > 0:
            node = stack.pop()
            if node.left == None and node.right == None:
                trav.append(node.val)
                visited.add(node)
            
            if node.left and node.left not in visited:
                stack.append(node)
                stack.append(node.left)
            elif node not in visited:
                trav.append(node.val)
                visited.add(node)
                if node.right and node.right not in visited:
                    stack.append(node.right)
        return trav
    
    
    def recursiveTraversal(self, root: 'TreeNode') -> List[int]:
        if not root:
            return []
        if root.left == None and root.right == None:
            return [root.val]
        trav = []
        if root.left:
            trav += self.recursiveTraversal(root.left)
        trav += [root.val]
        if root.right:
            trav += self.recursiveTraversal(root.right)
        return trav