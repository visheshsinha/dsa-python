# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.uniValue = -1
        
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        return self.checkUnivalue(root)
    
    def checkUnivalue(self, root):
        if root is None:
            return True
        
        if self.uniValue == -1:
            self.uniValue = root.val
        
        if root.val != self.uniValue:
            return False
        else:
            if root.left == None and root.right == None:
                return True
            
            return self.checkUnivalue(root.left) and self.checkUnivalue(root.right)