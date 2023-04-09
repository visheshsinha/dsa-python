'''
https://www.geeksforgeeks.org/queries-for-greatest-pair-sum-in-the-given-index-range-using-segment-tree/?ref=rp
'''

class SegmentTree:
    def __init__(self, nums):
        self.nums = nums
        self.length = len(nums)
        self.segmentTree = [{'maxValue': 0, 'greatestPairSum': 0}] * (self.length * 4)
        self.construct(start = 0, end = self.length - 1, currentIndex = 0)
    
    def construct(self, start: int, end: int, currentIndex: int) -> None:
        if start == end:
            self.segmentTree[currentIndex] = {
                'maxValue': self.nums[start],
                'greatestPairSum': 0
                }
            return
        
        mid = start + ((end - start) // 2)
        self.construct(start, mid, 2*currentIndex + 1)
        self.construct(mid + 1, end, 2*currentIndex + 2)

        self.segmentTree[currentIndex] = self.helper(self.segmentTree[2*currentIndex + 1] , self.segmentTree[2*currentIndex + 2])
        return

    def greatestPairSumQuery(self, left: int, right: int, start = 0, end = None, currentIndex = 0) -> object:
        if end == None:
            end = self.length - 1

        # no overlapping
        if start > right or end < left:
            return {'maxValue': -1, 'greatestPairSum': -1}
        
        # complete overlapping
        if start >= left and end <= right:
            return self.segmentTree[currentIndex]
        
        mid = start + ((end - start) // 2)
        leftPair = self.greatestPairSumQuery(left, right, start, mid, 2*currentIndex + 1)
        rightPair = self.greatestPairSumQuery(left, right, mid + 1, end, 2*currentIndex + 2)

        return self.helper(leftPair, rightPair)
    
    def helper(self, left: object, right: object) -> object:
        answer = {}
        answer['greatestPairSum'] = max(
            left['maxValue'] + right['maxValue'], max(
                                                        left['greatestPairSum'],
                                                        right['greatestPairSum']
                                                    )
        )

        answer['maxValue'] = max(left['maxValue'], right['maxValue'])

        return answer


if __name__ == '__main__':
    nums = list(map(int, input().split()))
    S = SegmentTree(nums)
    left, right = map(int, input().split())
    answer = S.greatestPairSumQuery(left, right)
    print(answer['greatestPairSum'])