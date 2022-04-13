# Subarrays with K Different Integers
# https://leetcode.com/problems/subarrays-with-k-different-integers/


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.subarrayWithAtmostKDistinct(
            nums, k
        ) - self.subarrayWithAtmostKDistinct(nums, k - 1)

    def subarrayWithAtmostKDistinct(self, nums, k):
        N = len(nums)

        answer = 0
        release = 0
        distinct = 0
        cache = {}

        for acquire in range(N):
            currentNum = nums[acquire]

            if currentNum in cache:
                cache[currentNum] += 1
            else:
                cache[currentNum] = 1
                distinct += 1

            while release <= acquire and distinct > k:
                discardNum = nums[release]
                release += 1
                cache[discardNum] -= 1

                if cache[discardNum] == 0:
                    del cache[discardNum]
                    distinct -= 1

            answer += acquire - release + 1

        return answer
