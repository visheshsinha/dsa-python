# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.sameTree(p, q)

    def sameTree(self, p, q):
        if p == None and q == None:
            return True
        elif p == None or q == None:
            return False
        else:
            if p.val != q.val:
                return False
            else:
                return self.sameTree(p.right, q.right) and self.sameTree(p.left, q.left)
