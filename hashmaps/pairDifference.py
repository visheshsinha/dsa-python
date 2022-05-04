class Solution:
    def findPair(self, nums, L, N):
        #code here
        nums.sort(reverse=True)
        cache = {}
        answer = -1
        
        for num in nums:
            
            currentKey = N + num
            
            if currentKey in cache:
                return True
            
            currentKey2 = num - N
            
            if currentKey2 in cache:
                return True
            
            cache[num] = True

        return False