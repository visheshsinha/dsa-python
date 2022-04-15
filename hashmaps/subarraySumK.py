# Subarray Sum Equals K
# https://leetcode.com/problems/subarray-sum-equals-k/


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        answer = 0
        cache = {0: 1}
        prefixSum = 0

        for num in nums:
            prefixSum += num
            currentKey = prefixSum - k

            if currentKey in cache:
                answer += cache[currentKey]

            if prefixSum in cache:
                cache[prefixSum] += 1
            else:
                cache[prefixSum] = 1

        return answer
