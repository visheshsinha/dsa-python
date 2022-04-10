class Solution:
    def __init__(self):
        self.cache = {}
        
    def longestPalindromeSubseq(self, s: str) -> int:
        return self.lcs(s, s[::-1], len(s), i=0, j=0)
    
    def lcs(self, text1, text2, N, i, j):
        if i >= N or j >= N:
            return 0
        
        currentKey = (i, j)
        
        if currentKey in self.cache:
            return self.cache[currentKey]
        
        answer = 0
        
        if text1[i] == text2[j]:
            answer = 1 + self.lcs(text1, text2, N, i + 1, j + 1)
        else:
            answer = max(self.lcs(text1, text2, N, i + 1, j), self.lcs(text1, text2, N, i, j + 1))
        
        self.cache[currentKey] = answer
        return self.cache[currentKey]