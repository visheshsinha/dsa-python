"""
Fibonacci Number
https://leetcode.com/problems/fibonacci-number/
"""


class Solution:
    def __init__(self):
        self.cache = {}

    def fib(self, n: int) -> int:
        return self.fibonacci(currentNum=n)

    def fibonacci(self, currentNum):

        if currentNum == 1:
            return 1
        elif currentNum <= 0:
            return 0

        if currentNum in self.cache:
            return self.cache[currentNum]

        self.cache[currentNum] = self.fibonacci(currentNum - 1) + self.fibonacci(
            currentNum - 2
        )
        return self.cache[currentNum]
