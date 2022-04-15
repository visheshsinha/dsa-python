# Equal 0, 1 and 2 
# https://practice.geeksforgeeks.org/problems/equal-0-1-and-23208/1/#

class Solution:
    def getSubstringWithEqual012(self, S):
        # code here
        answer = 0
        cache = {(0, 0): 1}
        
        z0 = z1 = z2 = 0
        
        for char in S:
            if char == "0":
                z0 += 1
            elif char == "1":
                z1 += 1
            else:
                z2 += 1
            
            currentKey = (z0 - z1, z1 - z2)
            
            if currentKey in cache:
                answer += cache[currentKey]
                cache[currentKey] += 1
            else:
                cache[currentKey] = 1
        
        return answer