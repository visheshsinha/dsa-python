class Solution:
    def __init__(self):
        self.cache = {}
        
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        
        return self.lcs(text1, text2, m, n, i=0, j=0)
    
    def lcs(self, text1, text2, m, n, i, j):
        if i >= m or j >= n:
            return 0
        
        currentKey = (i, j)
        
        if currentKey in self.cache:
            return self.cache[currentKey]
        
        answer = 0
        
        if text1[i] == text2[j]:
            answer = 1 + self.lcs(text1, text2, m, n, i + 1, j + 1)
        else:
            answer = max(self.lcs(text1, text2, m, n, i + 1, j), self.lcs(text1, text2, m, n, i, j + 1))
        
        self.cache[currentKey] = answer
        return self.cache[currentKey]