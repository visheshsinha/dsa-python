"""
Rod Cutting
https://practice.geeksforgeeks.org/problems/rod-cutting0840/1
"""


class Solution:
    def __init__(self):
        self.cache = {}

    def cutRod(self, price, N):
        return self.maxValue(price, N, currentIndex=0)

    def maxValue(self, price, N, currentIndex):

        if currentIndex >= len(price):
            return 0

        currentKey = (N, currentIndex)

        if currentKey in self.cache:
            return self.cache[currentKey]

        take = 0

        if currentIndex + 1 <= N:
            take = price[currentIndex] + self.maxValue(
                price, N - currentIndex - 1, currentIndex
            )

        notTake = self.maxValue(price, N, currentIndex + 1)

        self.cache[currentKey] = max(take, notTake)
        return self.cache[currentKey]
