"""
Climbing Stairs
https://leetcode.com/problems/climbing-stairs/submissions/
"""

class Solution:
    def __init__(self):
        self.cache = {}

    def climbStairs(self, n: int) -> int:
        return self.noOfWays(n, currentStair=0)

    def noOfWays(self, n, currentStair):

        if currentStair > n:
            return 0
        elif currentStair == n:
            return 1

        if currentStair in self.cache:
            return self.cache[currentStair]

        oneStep = self.noOfWays(n, currentStair + 1)
        twoStep = self.noOfWays(n, currentStair + 2)

        self.cache[currentStair] = oneStep + twoStep
        return self.cache[currentStair]
