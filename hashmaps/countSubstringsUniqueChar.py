class Solution:
    def countSubstrings(self, s):

        answer = 0
        cache = {}
        release = 0

        for acquire in range(len(s)):
            currentChar = s[acquire]

            while release < acquire and currentChar in cache:
                # Releasing element until we release the currentChar which is present beforehand in our cache
                discardChar = s[release]
                cache[discardChar] -= 1

                if cache[discardChar] == 0:
                    del cache[discardChar]

                release += 1

            cache[currentChar] = 1
            answer += (
                acquire - release + 1
            )  # counting substrings with all unique characters

        return answer


if __name__ == "__main__":

    obj = Solution()
    print(obj.countSubstrings(input()))
