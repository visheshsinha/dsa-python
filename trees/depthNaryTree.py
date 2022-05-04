"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(self, root: "Node") -> int:
        return self.calculateDepth(root)

    def calculateDepth(self, root):
        if root == None:
            return 0

        answer = 0
        for child in root.children:
            answer = max(answer, self.calculateDepth(child))

        return answer + 1
