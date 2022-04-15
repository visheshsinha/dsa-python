# Longest Subarray With Equal Number Of 0s 1s And 2s
# https://www.pepcoding.com/resources/data-structures-and-algorithms-in-java-levelup/hashmap-and-heaps/longest-subarray-with-equal-number-of-0s-1s-and-2s-official/ojquestion

class Solution:
    def longestArray(self, nums):

        answer = 0
        cache = {(0, 0): -1}
        z0 = z1 = z2 = 0

        for i in range(len(nums)):
            num = nums[i]
            if num == 0:
                z0 += 1
            elif num == 1:
                z1 += 1
            else:
                z2 += 1

            currentKey = (z0-z1, z1-z2)

            if currentKey in cache:
                answer = max(answer, i - cache[currentKey])
            else:
                cache[currentKey] = i
            
        return answer

if __name__ == "__main__":
    obj = Solution()
    N = int(input())
    nums = list(map(int, input().split()))
    print(obj.longestArray(nums))