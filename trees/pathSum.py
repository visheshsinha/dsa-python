# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.pathSum(root, targetSum, currentSum=0)

    def pathSum(self, root, targetSum, currentSum):
        if root == None:
            return False

        currentSum += root.val

        if root.right == None and root.left == None:
            if targetSum == currentSum:
                return True
            else:
                return False

        return self.pathSum(root.left, targetSum, currentSum) or self.pathSum(
            root.right, targetSum, currentSum
        )
