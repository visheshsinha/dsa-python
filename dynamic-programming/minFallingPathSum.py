from sys import maxsize

class Solution:
    def __init__(self):
        self.cache = {}
        
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        answer = maxsize
        
        N = len(matrix)
        
        for currentCol in range(N):
            answer = min(answer, self.minSum(matrix, N, currentRow=0, currentCol=currentCol))
        
        return answer
    
    def minSum(self, matrix, N, currentRow, currentCol):
        if currentRow >= N or currentCol >= N or currentCol < 0:
            return maxsize
        
        if currentRow == N-1:
            return matrix[currentRow][currentCol]
        
        currentKey = (currentRow, currentCol)
        
        if currentKey in self.cache:
            return self.cache[currentKey]
        
        down = self.minSum(matrix, N, currentRow + 1, currentCol)
        downRight = self.minSum(matrix, N, currentRow + 1, currentCol + 1)
        downLeft = self.minSum(matrix, N, currentRow + 1, currentCol - 1)
        
        self.cache[currentKey] = min(down, downRight, downLeft) + matrix[currentRow][currentCol]
        return self.cache[currentKey]
    
    