"""
House Robber
https://leetcode.com/problems/house-robber/
"""


class Solution:
    def __init__(self):
        self.cache = {}

    def rob(self, nums: List[int]) -> int:
        return self.maxRob(nums, currentIndex=0)

    def maxRob(self, nums, currentIndex):
        if currentIndex >= len(nums):
            return 0

        if currentIndex in self.cache:
            return self.cache[currentIndex]

        rob = self.maxRob(nums, currentIndex + 2) + nums[currentIndex]
        dontRob = self.maxRob(nums, currentIndex + 1)

        self.cache[currentIndex] = max(rob, dontRob)

        return self.cache[currentIndex]
