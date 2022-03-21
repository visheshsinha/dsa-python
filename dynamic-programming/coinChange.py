"""
Coin Change
https://leetcode.com/problems/coin-change/
"""


from sys import maxsize

class Solution:
    def __init__(self):
        self.cache = {}
        
    def coinChange(self, coins: List[int], amount: int) -> int:
        answer = self.minCoins(coins, amount, currentIndex=0)
        
        if answer == maxsize:
            return -1
        else:
            return answer
    
    def minCoins(self, coins, amount, currentIndex):
        
        if amount == 0:
            return 0
        
        if currentIndex >= len(coins):
            return maxsize
        
        currentKey = (amount, currentIndex)
        
        if currentKey in self.cache:
            return self.cache[currentKey]
        
        take = maxsize
        
        if coins[currentIndex] <= amount:
            take = 1 + self.minCoins(coins, amount - coins[currentIndex], currentIndex)
        
        notTake = self.minCoins(coins, amount, currentIndex + 1)
        
        self.cache[currentKey] = min(take, notTake)
        return self.cache[currentKey]