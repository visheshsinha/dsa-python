# https://leetcode.com/problems/range-frequency-queries/

from collections import defaultdict
from itertools import chain

class SegmentTree:
    def __init__(self, nums) -> None:
        self.nums = nums
        self.length = len(nums)
        self.segmentTree = [defaultdict(lambda: 0) for _ in range(self.length * 4)]
        self.construct(start = 0, end = self.length - 1, currentIndex = 0)
    
    def construct(self, start, end, currentIndex):
        if start == end:
            self.segmentTree[currentIndex][self.nums[start]] += 1 # can do = 1 as well as it will be same
            return
        
        mid = start + ((end - start) // 2)
        self.construct(start, mid, 2 * currentIndex + 1)
        self.construct(mid + 1, end, 2 * currentIndex + 2)
        
        self.segmentTree[currentIndex] = self.helper(self.segmentTree[2 * currentIndex + 1], self.segmentTree[2 * currentIndex + 2])
        return
    
    def rangeFreq(self, left, right, value, start = 0, end = None, currentIndex = 0):
        if end == None:
            end = self.length - 1
        
        # no overlapping
        if start > right or end < left:
            return 0
        
        # complete overlapping
        if start >= left and end <= right:
            return self.segmentTree[currentIndex][value]
        
        mid = start + ((end - start) // 2)
        leftPair = self.rangeFreq(left, right, value, start, mid, 2*currentIndex + 1)
        rightPair = self.rangeFreq(left, right, value, mid + 1, end, 2*currentIndex + 2)

        return leftPair + rightPair
    
    def helper(self, leftPair, rightPair):
        answer = collections.defaultdict(lambda: 0)
        
        for key, val in chain(leftPair.items(), rightPair.items()):
            answer[key] += val
        
        answer1 = copy.deepcopy(answer)
        return answer1


class RangeFreqQuery:
    def __init__(self, arr: list):
        self.S = SegmentTree(nums = arr)

    def query(self, left: int, right: int, value: int) -> int:
        return self.S.rangeFreq(left, right, value)


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)