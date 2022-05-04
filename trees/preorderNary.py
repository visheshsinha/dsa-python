"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def __init__(self):
        self.answer = []
    
    def preorder(self, root: 'Node') -> List[int]:
        self.preorderTraversal(root)
        return self.answer
    
    def preorderTraversal(self, root):
        if root is None:
            return 
        
        self.answer.append(root.val)
        
        for child in root.children:
            self.preorderTraversal(child)
        
        return