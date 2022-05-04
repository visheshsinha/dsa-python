# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.answer = []
        
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.rootToLeaf(root, "")
        answer = 0
        for i in self.answer:
            answer += int(i, 2)
        return answer
    
    def rootToLeaf(self, root, current):
        if root == None:
            return
        
        if root.right == None and root.left == None:
            self.answer.append(current + str(root.val))
            return
        
        current += str(root.val)
        self.rootToLeaf(root.left, current)
        self.rootToLeaf(root.right, current)
        
        return