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
        
    def postorder(self, root: 'Node') -> List[int]:
        self.postorderTraversal(root)
        return self.answer
    
    def postorderTraversal(self, root):
        if root is None:
            return 
        
        for child in root.children:
            self.postorderTraversal(child)
        self.answer.append(root.val)
        
        return