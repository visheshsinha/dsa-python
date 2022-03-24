""" 
Jump Game 
https://leetcode.com/problems/jump-game/
"""


class Solution:
    def __init__(self):
        self.cache = {}

    def canJump(self, nums: List[int]) -> bool:
        return self.isPossible(nums, currentIndex=0)

    def isPossible(self, nums, currentIndex):
        if currentIndex >= len(nums):
            return False

        if currentIndex == len(nums) - 1:
            return True

        if currentIndex in self.cache:
            return self.cache[currentIndex]

        for i in range(1, nums[currentIndex] + 1):
            if self.isPossible(nums, currentIndex + i):
                self.cache[currentIndex] = True
                return self.cache[currentIndex]

        self.cache[currentIndex] = False
        return self.cache[currentIndex]
