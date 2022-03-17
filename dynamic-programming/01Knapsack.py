"""
0 - 1 Knapsack Problem
https://practice.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1
"""


class Solution:
    def __init__(self):
        self.cache = {}

    # Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self, W, wt, val, n):
        # code here
        return self.maxProfit(W, wt, val, n, currentIndex=0)

    def maxProfit(self, W, wt, val, n, currentIndex):

        if currentIndex >= n:
            return 0

        currentKey = (W, currentIndex)

        if currentKey in self.cache:
            return self.cache[currentKey]

        take = 0

        if W >= wt[currentIndex]:
            take = (
                self.maxProfit(W - wt[currentIndex], wt, val, n, currentIndex + 1)
                + val[currentIndex]
            )

        notTake = self.maxProfit(W, wt, val, n, currentIndex + 1)

        self.cache[currentKey] = max(take, notTake)
        return self.cache[currentKey]
