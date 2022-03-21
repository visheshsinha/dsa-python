"""
Knapsack with Duplicate Items / Unbounded Knapsack
https://practice.geeksforgeeks.org/problems/knapsack-with-duplicate-items4201/1
"""


class Solution:
    def __init__(self):
        self.cache = {}

    def knapSack(self, N, W, val, wt):
        # code here
        return self.maxProfit(N, W, val, wt, currentIndex=0)

    def maxProfit(self, N, W, val, wt, currentIndex):
        if currentIndex >= N:
            return 0

        currentKey = (W, currentIndex)

        if currentKey in self.cache:
            return self.cache[currentKey]

        take = 0

        if wt[currentIndex] <= W:
            take = val[currentIndex] + self.maxProfit(
                N, W - wt[currentIndex], val, wt, currentIndex
            )

        notTake = self.maxProfit(N, W, val, wt, currentIndex + 1)

        self.cache[currentKey] = max(take, notTake)
        return self.cache[currentKey]
