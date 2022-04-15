# Longest Sub-Array with Sum K
# https://practice.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1

class Solution:
    def lenOfLongSubarr(self, nums, N, k):
        # Complete the function

        answer = 0
        cache = {0: -1}
        prefixSum = 0

        for i in range(N):
            num = nums[i]
            prefixSum += num
            currentKey = prefixSum - k

            if currentKey in cache:
                answer = max(answer, i - cache[currentKey])

            if prefixSum in cache:
                continue
            else:
                cache[prefixSum] = i

        return answer
