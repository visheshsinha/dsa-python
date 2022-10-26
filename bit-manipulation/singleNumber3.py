class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        xorAns = 0
        
        for num in nums:
            xorAns ^= num
        
        # 110 & -110 = 010
        xorAns &= -xorAns
        
        answer = [0, 0]
        
        for num in nums:
            
            if (num & xorAns) == 0:
                answer[0] ^= num
            else:
                answer[1] ^= num
        
        return answer