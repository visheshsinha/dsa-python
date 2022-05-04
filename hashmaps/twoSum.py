class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        cache = collections.defaultdict(list)
        
        for i in range(len(nums)):
            currentNum = nums[i]
            cache[currentNum].append(i)
        
        for i in range(len(nums)):
            currentNum = nums[i]
            
            if target - currentNum in cache:
                if target - currentNum == currentNum:
                    if len(cache[currentNum]) >= 2:
                        return cache[currentNum][:2]
                    else:
                        continue
                else:
                    return [cache[currentNum][0], cache[target - currentNum][0]]
        
        return []