class Solution:

    # Function to count subarrays with 1s and 0s.
    def countSubarrWithEqualZeroAndOne(self, arr, n):
        # Your code here
        prefixSum = 0
        cache = {0: 1}
        answer = 0

        for i in range(n):
            currentElement = arr[i]

            if currentElement:
                prefixSum += 1
            else:
                prefixSum -= 1

            if prefixSum in cache:
                answer += cache[prefixSum]
                cache[prefixSum] += 1
            else:
                cache[prefixSum] = 1

        return answer
