class SegmentTree:
    def __init__(self, nums):
        self.nums = nums
        self.length = len(nums)
        self.segmentTree = [0] * (self.length * 4)
        self.constructSegmentTree(start = 0, end = self.length - 1, currentIndex = 0)
    
    def constructSegmentTree(self, start, end, currentIndex):
        if start == end:
            self.segmentTree[currentIndex] = self.nums[start]
            return
        
        mid = start + ((end - start) // 2)
        self.constructSegmentTree(start, mid, 2 * currentIndex + 1)
        self.constructSegmentTree(mid+1, end, 2 * currentIndex + 2)
        
        self.segmentTree[currentIndex] = self.segmentTree[2 * currentIndex + 1] + self.segmentTree[2 * currentIndex + 2]
        return
    
    def updateSegmentTree(self, index, value, start = 0, end = None, currentIndex = 0):
        if end == None:
            end = self.length - 1
        
        if currentIndex == 0:
            self.nums[index] = value
        
        if start == end:
            self.segmentTree[currentIndex] = self.nums[index]
            return
        
        mid = start + ((end - start) // 2)

        if mid < index:
            self.updateSegmentTree(index, value, mid + 1, end, 2 * currentIndex + 2)
        else:
            self.updateSegmentTree(index, value, start, mid, 2 * currentIndex + 1)

        self.segmentTree[currentIndex] = self.segmentTree[2 * currentIndex + 1] + self.segmentTree[2 * currentIndex + 2]
        return
    
    def getRangeSum(self, left, right, start = 0, end = None, currentIndex = 0):
        if end == None:
            end = self.length - 1
        
        # no overlapping
        if start > right or end < left:
            return 0
        # complete overlapping
        elif start >= left and end <= right:
            return self.segmentTree[currentIndex]
        # partial overlapping
        else:
            mid = start + ((end - start) // 2)
            leftSum = self.getRangeSum(left, right, start, mid, 2 * currentIndex + 1)
            rightSum = self.getRangeSum(left, right, mid+1, end, 2 * currentIndex + 2)
            
            return leftSum + rightSum
            

class NumArray:
    def __init__(self, nums: List[int]):
        self.S = SegmentTree(nums)
        self.nums = nums
        self.length = len(nums)

    def update(self, index: int, val: int) -> None:
        self.nums[index] = val
        self.S.updateSegmentTree(index, val)
        return

    def sumRange(self, left: int, right: int) -> int:
        return self.S.getRangeSum(left, right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)