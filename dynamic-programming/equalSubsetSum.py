"""
Partition Equal Subset Sum
https://leetcode.com/problems/partition-equal-subset-sum/
"""


class Solution:
    def __init__(self):
        self.cache = {}

    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)

        if totalSum % 2 != 0:
            return False

        return self.targetSum(nums, currentIndex=0, target=totalSum // 2)

    def targetSum(self, nums, currentIndex, target):

        if target == 0:
            return True

        if currentIndex >= len(nums):
            return False

        currentKey = (currentIndex, target)

        if currentKey in self.cache:
            return self.cache[currentKey]

        take = False

        if target >= nums[currentIndex]:
            take = self.targetSum(nums, currentIndex + 1, target - nums[currentIndex])

        notTake = self.targetSum(nums, currentIndex + 1, target)

        self.cache[currentKey] = take or notTake
        return self.cache[currentKey]
