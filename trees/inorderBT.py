# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.answer = []
        
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.inorder(root)
        return self.answer
    
    def inorder(self, root):
        if root is None:
            return 
        
        self.inorder(root.left)
        self.answer.append(root.val)
        self.inorder(root.right)
        
        return