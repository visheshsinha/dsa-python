"""
Target Sum
https://leetcode.com/problems/target-sum/
"""

class Solution:
    def __init__(self):
        self.cache = {}

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return self.achieveTarget(nums, target, currentIndex=0)

    def achieveTarget(self, nums, target, currentIndex):

        if currentIndex >= len(nums):
            if target == 0:
                return 1
            return 0

        currentKey = (currentIndex, target)

        if currentKey in self.cache:
            return self.cache[currentKey]

        positive = self.achieveTarget(
            nums, target + nums[currentIndex], currentIndex + 1
        )
        negative = self.achieveTarget(
            nums, target - nums[currentIndex], currentIndex + 1
        )

        self.cache[currentKey] = positive + negative

        return self.cache[currentKey]
