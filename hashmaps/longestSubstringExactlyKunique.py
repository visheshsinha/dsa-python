# Longest K unique characters substring
# https://practice.geeksforgeeks.org/problems/longest-k-unique-characters-substring0853/1/#


class Solution:
    def longestKSubstr(self, s, k):

        answer = -1
        distinct = 0
        release = 0

        cache = {}

        for acquire in range(len(s)):

            currentChar = s[acquire]

            if currentChar in cache:
                cache[currentChar] += 1
            else:
                cache[currentChar] = 1
                distinct += 1

            while release < acquire and distinct > k:

                discardChar = s[release]
                release += 1
                cache[discardChar] -= 1

                if cache[discardChar] == 0:
                    del cache[discardChar]
                    distinct -= 1

            if distinct == k:
                answer = max(answer, acquire - release + 1)

        return answer
