class Solution:
    def maxLen(self, n, arr):
        #Code here
        prefixSum = 0 
        answer = 0
        
        cache = {0: -1}
        
        for i in range(n):
            prefixSum += arr[i]
            
            if prefixSum in cache:
                answer = max(answer, i - cache[prefixSum])
            else:
                cache[prefixSum] = i
        
        return answer