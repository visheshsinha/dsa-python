class Solution:
    def longSubarrWthSumDivByK (self, nums, n, k) : 
		#Complete the function
        
        answer = 0
        cache = {0: -1}
        
        prefixSum = 0
        
        for i in range(n):
            num = nums[i]
            prefixSum += num
            currentKey = prefixSum % k
            
            if currentKey in cache:
                answer = max(answer, i - cache[currentKey])
            else:
                cache[currentKey] = i
        
        return answer