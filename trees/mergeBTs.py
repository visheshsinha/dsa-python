# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        return self.mergeBT(node1=root1, node2=root2)

    def mergeBT(self, node1, node2):
        if node1 == None and node2 == None:
            return None
        elif node1 is None:
            return node2
        elif node2 is None:
            return node1
        else:
            node1.val = node1.val + node2.val
            node1.left = self.mergeBT(node1.left, node2.left)
            node1.right = self.mergeBT(node1.right, node2.right)
            return node1
