# Count Of Substrings Having At Most K Unique Characters
# https://www.pepcoding.com/resources/data-structures-and-algorithms-in-java-levelup/hashmap-and-heaps/count-of-substrings-having-at-most-k-unique-characters-official/ojquestion


class Solution:
    def atmostKunique(self, s, k):
        
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
            
            while release < acquire and distinct > k:
                discardChar = s[release]
                release += 1
                cache[discardChar] -= 1

                if cache[discardChar] == 0:
                    del cache[discardChar]
                    distinct -= 1
            
            answer += acquire - release + 1
        
        return answer


if __name__ == "__main__":
    obj = Solution()
    s = input()
    k = int(input())
    print(obj.atmostKunique(s, k))