def countSubarrays(N: int, nums: List[int]) -> int:
    # Write your code here.
    prefixSum = 0
    answer = 0
    
    cache = {0: 1}
    
    for num in nums:
        prefixSum += num
        
        if prefixSum in cache:
            answer += cache[prefixSum]
            cache[prefixSum] += 1
        else:
            cache[prefixSum] = 1
    
    return answer