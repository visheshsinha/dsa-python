from sys import maxsize


class Solution:
    def __init__(self):
        self.cache = {}

    def minPathSum(self, grid: List[List[int]]) -> int:
        return self.minSum(
            grid, m=len(grid), n=len(grid[0]), currentRow=0, currentCol=0
        )

    def minSum(self, grid, m, n, currentRow, currentCol):
        if currentRow >= m or currentCol >= n:
            return maxsize

        if currentRow == m - 1 and currentCol == n - 1:
            return grid[currentRow][currentCol]

        currentKey = (currentRow, currentCol)

        if currentKey in self.cache:
            return self.cache[currentKey]

        down = self.minSum(grid, m, n, currentRow + 1, currentCol)
        right = self.minSum(grid, m, n, currentRow, currentCol + 1)

        self.cache[currentKey] = min(down, right) + grid[currentRow][currentCol]
        return self.cache[currentKey]
