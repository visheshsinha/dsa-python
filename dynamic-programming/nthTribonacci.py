"""
N-th Tribonacci Number
https://leetcode.com/problems/n-th-tribonacci-number/
"""


class Solution:
    def __init__(self):
        self.cache = {}

    def tribonacci(self, n: int) -> int:
        return self.nthtribonacci(currentNum=n)

    def nthtribonacci(self, currentNum):

        if currentNum == 0:
            return 0
        elif currentNum in (2, 1):
            return 1

        if currentNum in self.cache:
            return self.cache[currentNum]

        self.cache[currentNum] = (
            self.nthtribonacci(currentNum - 1)
            + self.nthtribonacci(currentNum - 2)
            + self.nthtribonacci(currentNum - 3)
        )

        return self.cache[currentNum]
