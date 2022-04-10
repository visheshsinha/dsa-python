class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        answer = []
        cache = {}
        
        for num in nums2:
            if num in cache:
                cache[num] += 1
            else:
                cache[num] = 1
                
        for num in nums1:
            if num in cache: 
                answer.append(num)
                cache[num] -= 1
                
                if cache[num] == 0:
                    del cache[num]
        
        return answer