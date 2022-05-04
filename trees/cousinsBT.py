# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.parents = [None, None]
        self.levels = [0, 0]

    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        self.findParentLevel(root, x, y, currentParent=None, currentLevel=0)
        return self.parents[0] != self.parents[1] and self.levels[0] == self.levels[1]

    def findParentLevel(self, root, x, y, currentParent, currentLevel):
        if root == None:
            return

        if root.val == x:
            self.parents[0] = currentParent
            self.levels[0] = currentLevel
            return
        elif root.val == y:
            self.parents[1] = currentParent
            self.levels[1] = currentLevel
            return
        else:
            currentLevel += 1
            currentParent = root
            self.findParentLevel(root.left, x, y, currentParent, currentLevel)
            self.findParentLevel(root.right, x, y, currentParent, currentLevel)
            return
