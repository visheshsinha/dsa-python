"""
Min Cost Climbing Stairs
https://leetcode.com/problems/min-cost-climbing-stairs/
"""


class Solution:
    def __init__(self):
        self.cache = {}

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return min(
            self.minCost(cost, currentIndex=0), self.minCost(cost, currentIndex=1)
        )

    def minCost(self, cost, currentIndex):

        if currentIndex >= len(cost):
            return 0

        if currentIndex in self.cache:
            return self.cache[currentIndex]

        oneStep = self.minCost(cost, currentIndex + 1) + cost[currentIndex]
        twoStep = self.minCost(cost, currentIndex + 2) + cost[currentIndex]

        self.cache[currentIndex] = min(oneStep, twoStep)

        return self.cache[currentIndex]
