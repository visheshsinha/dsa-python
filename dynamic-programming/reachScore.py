"""
Reach a given score
https://practice.geeksforgeeks.org/problems/reach-a-given-score-1587115621/1
"""


def count(n):
    # your code here
    nums = [3, 5, 10]
    return noOfWays(nums, target=n, currentIndex=0, cache={})


def noOfWays(nums, target, currentIndex, cache):
    if target == 0:
        return 1

    if currentIndex >= len(nums):
        return 0

    currentKey = (currentIndex, target)

    if currentKey in cache:
        return cache[currentKey]

    take = 0

    if target >= nums[currentIndex]:
        take = noOfWays(nums, target - nums[currentIndex], currentIndex, cache)

    notTake = noOfWays(nums, target, currentIndex + 1, cache)

    cache[currentKey] = notTake + take
    return cache[currentKey]
