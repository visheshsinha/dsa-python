class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        cache = {}
        
        for char in s:
            if char in cache:
                cache[char] += 1
            else:
                cache[char] = 1
        
        for char in t:
            if char in cache:
                cache[char] -= 1
                
                if cache[char] == 0:
                    del cache[char]
            else:
                return False
        
        return len(cache) == 0