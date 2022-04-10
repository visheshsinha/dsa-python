class Solution:
    def __init__(self):
        self.cache = {}
        
    def minDistance(self, word1: str, word2: str) -> int:
        return self.editDistance(word1, word2, m=len(word1), n=len(word2), currentIndex1=0, currentIndex2=0)
    
    def editDistance(self, word1, word2, m, n, currentIndex1, currentIndex2):
        if currentIndex2 >= n:
            return (m - currentIndex1)  # leftover word1 characters to be deleted
        
        if currentIndex1 >= m:
            return (n - currentIndex2)  # leftover word2 characters to be inserted in word1
        
        currentKey = (currentIndex1, currentIndex2)
        
        if currentKey in self.cache:
            return self.cache[currentKey]
        
        answer = 0
        
        if word1[currentIndex1] == word2[currentIndex2]:
            answer = self.editDistance(word1, word2, m, n, currentIndex1 + 1, currentIndex2 + 1)
        else:
            
            answer = 1 + min(
            
                self.editDistance(word1, word2, m, n, currentIndex1 + 1, currentIndex2), # deletion
                self.editDistance(word1, word2, m, n, currentIndex1, currentIndex2 + 1), # insertion
                self.editDistance(word1, word2, m, n, currentIndex1 + 1, currentIndex2 + 1) # replace
                
            )
            
        self.cache[currentKey] = answer
        return self.cache[currentKey]