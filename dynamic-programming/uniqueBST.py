class Solution:
    def __init__(self):
        self.cache = {}

    def numTrees(self, n: int) -> int:
        return self.nthCatalan(n)

    def nthCatalan(self, n):

        if n <= 1:
            return 1

        if n in self.cache:
            return self.cache[n]

        answer = 0

        for i in range(n):
            temp = self.nthCatalan(i) * self.nthCatalan(n - i - 1)
            answer += temp

        self.cache[n] = answer

        return self.cache[n]
