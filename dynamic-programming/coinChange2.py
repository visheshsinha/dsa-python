"""
Coin Change 2
https://leetcode.com/problems/coin-change-2/
"""


class Solution:
    def __init__(self):
        self.cache = {}

    def change(self, amount: int, coins: List[int]) -> int:
        return self.noOfCombinations(coins, amount, currentIndex=0)

    def noOfCombinations(self, coins, amount, currentIndex):
        if amount == 0:
            return 1

        if currentIndex >= len(coins):
            return 0

        currentKey = (amount, currentIndex)

        if currentKey in self.cache:
            return self.cache[currentKey]

        take = 0

        if coins[currentIndex] <= amount:
            take = self.noOfCombinations(
                coins, amount - coins[currentIndex], currentIndex
            )

        notTake = self.noOfCombinations(coins, amount, currentIndex + 1)

        self.cache[currentKey] = take + notTake
        return self.cache[currentKey]
