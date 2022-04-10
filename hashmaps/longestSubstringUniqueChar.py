class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        cache = {}
        answer = 0
        release = 0

        for acquire in range(len(s)):
            currentChar = s[acquire]

            while release < acquire and currentChar in cache:
                discardChar = s[release]
                release += 1

                cache[discardChar] -= 1
                if cache[discardChar] == 0:
                    del cache[discardChar]

            cache[currentChar] = 1
            answer = max(answer, acquire - release + 1)

        return answer
