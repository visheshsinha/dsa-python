class Solution:
    def __init__(self):
        self.cache = {}

    # Function to find the nth catalan number.
    def findCatalan(self, n):
        # return the nth Catalan number.
        return self.catalan(n)

    def catalan(self, n):

        if n <= 1:
            return 1

        if n in self.cache:
            return self.cache[n]

        answer = 0

        for i in range(n):
            answer += self.catalan(i) * self.catalan(n - i - 1)

        self.cache[n] = answer
        return self.cache[n]
