"""
Jump Game II	
https://leetcode.com/problems/jump-game-ii/
"""

from sys import maxsize


class Solution:
    def __init__(self):
        self.cache = {}

    def jump(self, nums: List[int]) -> int:
        return self.minJumps(nums, currentIndex=0)

    def minJumps(self, nums, currentIndex):

        if currentIndex >= len(nums) - 1:
            return 0

        if currentIndex in self.cache:
            return self.cache[currentIndex]

        answer = maxsize

        for i in range(1, nums[currentIndex] + 1):
            answer = min(answer, self.minJumps(nums, currentIndex + i) + 1)

        self.cache[currentIndex] = answer
        return self.cache[currentIndex]
