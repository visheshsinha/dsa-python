class Solution:
    def __init__(self):
        self.cache = {}

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        answer = 0

        for currentRow in range(m):
            for currentCol in range(n):

                if matrix[currentRow][currentCol] == "1":
                    answer = max(
                        answer, self.maxLength(matrix, m, n, currentRow, currentCol)
                    )

        return answer ** 2

    def maxLength(self, matrix, m, n, currentRow, currentCol):

        if currentRow >= m or currentCol >= n or matrix[currentRow][currentCol] == "0":
            return 0

        currentKey = (currentRow, currentCol)

        if currentKey in self.cache:
            return self.cache[currentKey]

        down = self.maxLength(matrix, m, n, currentRow + 1, currentCol)
        right = self.maxLength(matrix, m, n, currentRow, currentCol + 1)
        downRight = self.maxLength(matrix, m, n, currentRow + 1, currentCol + 1)

        self.cache[currentKey] = 1 + min(down, right, downRight)
        return self.cache[currentKey]
