# Substring With At Least K Distinct Characters
# https://www.lintcode.com/problem/1375/description


class Solution:
    """
    No. of substrings = n * (n + 1) / 2
    No. of substrings = substrings with more than k distinct chars +
                            substrings with exactly k distinct chars +
                            substrings with less than k distinct chars

    Previous Code we wrote was of atmost K (exactly K + less than K)
    """

    def k_distinct_characters(self, s: str, k: int) -> int:
        # Write your code here
        answer = 0
        distinct = 0
        release = 0
        N = len(s)
        cache = {}
        k -= 1  # This makes it atmost k-1 distinct characters

        for acquire in range(N):

            currentChar = s[acquire]

            if currentChar in cache:
                cache[currentChar] += 1
            else:
                cache[currentChar] = 1
                distinct += 1

            while release <= acquire and distinct > k:

                discardChar = s[release]
                release += 1
                cache[discardChar] -= 1

                if cache[discardChar] == 0:
                    del cache[discardChar]
                    distinct -= 1

            answer += acquire - release + 1

        return (
            (N * (N + 1)) // 2
        ) - answer  # This gives us more than k-1 (which is atleast k = exactly k + more than k)
