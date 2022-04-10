class Solution:
    def __init__(self):
        self.cache = {}
        
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        return self.countPaths(obstacleGrid, m, n, currentRow=0, currentCol=0)
    
    def countPaths(self,obstacleGrid, m, n, currentRow, currentCol):
        if currentRow >= m or currentCol >= n or obstacleGrid[currentRow][currentCol] == 1:
            return 0
        
        if currentRow == m - 1 and currentCol == n - 1:
            return 1
        
        currentKey = (currentRow, currentCol)
        
        if currentKey in self.cache:
            return self.cache[currentKey]
        
        down = self.countPaths(obstacleGrid, m, n, currentRow + 1, currentCol)
        right = self.countPaths(obstacleGrid, m, n, currentRow, currentCol + 1)
        
        self.cache[currentKey] = down + right
        return self.cache[currentKey]