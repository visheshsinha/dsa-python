# Longest Substring with At Most K Distinct Characters
# https://www.lintcode.com/problem/386/

class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """

    def length_of_longest_substring_k_distinct(self, s: str, k: int) -> int:
        # write your code here
        answer = 0
        distinct = 0
        cache = {}

        release = 0

        for acquire in range(len(s)):

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

            answer = max(answer, acquire - release + 1)

        return answer
