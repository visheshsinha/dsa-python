"""
Unique Paths
https://leetcode.com/problems/unique-paths/
"""


class Solution:
    def __init__(self):
        self.cache = {}

    def uniquePaths(self, m: int, n: int) -> int:
        return self.countPaths(m, n, currentRow=0, currentCol=0)

    def countPaths(self, m, n, currentRow, currentCol):

        if currentRow >= m or currentCol >= n:
            return 0

        if currentRow == m - 1 and currentCol == n - 1:
            return 1

        currentKey = (currentRow, currentCol)

        if currentKey in self.cache:
            return self.cache[currentKey]

        down = self.countPaths(m, n, currentRow + 1, currentCol)
        right = self.countPaths(m, n, currentRow, currentCol + 1)

        self.cache[currentKey] = down + right
        return self.cache[currentKey]
