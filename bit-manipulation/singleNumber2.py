class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        ones, twos, threes = 0, 0, 0
        
        for num in nums:
            
            twos |= ones & num
            ones ^= num
            threes = ones & twos
            
            twos = ~threes & twos
            ones = ~threes & ones
        
        return ones