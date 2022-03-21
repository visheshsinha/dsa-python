"""
Delete and Earn
https://leetcode.com/problems/delete-and-earn/
"""


class Solution:
    def __init__(self):
        self.cache = {}

    def deleteAndEarn(self, nums: List[int]) -> int:

        nums = sorted(nums)
        maxValue = nums[-1]
        freq = [0] * (maxValue + 1)

        for num in nums:
            freq[num] += 1

        return self.maxPoints(freq, currentIndex=0)

    def maxPoints(self, freq, currentIndex):

        if currentIndex >= len(freq):
            return 0

        if currentIndex in self.cache:
            return self.cache[currentIndex]

        delete = (currentIndex * freq[currentIndex]) + self.maxPoints(
            freq, currentIndex + 2
        )
        notDelete = self.maxPoints(freq, currentIndex + 1)

        self.cache[currentIndex] = max(delete, notDelete)

        return self.cache[currentIndex]
