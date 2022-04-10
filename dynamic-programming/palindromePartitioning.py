from sys import maxsize


class Solution:
    def __init__(self):
        self.cache = {}

    def minCut(self, s: str) -> int:
        return self.minimumCut(s, start=0, end=len(s) - 1)

    def minimumCut(self, s, start, end):
        if self.isPalindrome(s, start, end):
            return 0

        currentKey = start

        if currentKey in self.cache:
            return self.cache[currentKey]

        answer = maxsize

        for i in range(start, end):
            if self.isPalindrome(s, start, i):
                answer = min(answer, 1 + self.minimumCut(s, i + 1, end))

        self.cache[currentKey] = answer
        return self.cache[currentKey]

    def isPalindrome(self, s, start, end):
        while start <= end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return False
        return True
