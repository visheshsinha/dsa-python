class Solution:
    def maxLen(self, arr, N):
        # code here
        prefixSum = 0
        cache = {0: -1}
        answer = 0

        for i in range(N):
            currentElement = arr[i]

            if currentElement:
                prefixSum += 1
            else:
                prefixSum -= 1

            if prefixSum in cache:
                answer = max(answer, i - cache[prefixSum])
            else:
                cache[prefixSum] = i

        return answer
