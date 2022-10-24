# Find no. of the set bits in a binary representation

class Solution:
    def __init__(self) -> None:
        self.table = [0] * 256
        self.initialize()
    
    # Using Non Bitwise Naive Method
    def naiveMethod(self, n) -> int: # O(N)
        count = 0

        while n != 0:
            if n % 2 == 1:
                count += 1
            n = n // 2
        
        return count

    # Using Bitwise Naive Method
    def bitwiseNaive(self, n) -> int: # O(N) - slightly faster
        count = 0

        while n != 0:
            if n & 1:
                count += 1
            n = n >> 1
        
        return count
    
    def brain_kerningam(self, n) -> int: # O(no. of Set Bits)
        count = 0

        while n != 0:
            n = n & (n - 1)
            count += 1
        
        return count

    def lookupTable(self, n) -> int: # O(1) - also has constant space complexity
        count = 0

        for _ in range(4):
            count += self.table[ n & 255 ]
            n = n >> 8
        
        return count
    
    def initialize(self):
        for i in range(1, 256):
            self.table[i] = self.table[ i >> 1 ] + (i & 1)


if __name__ == "__main__":
    solution = Solution()
    n = int(input())

    # print(solution.naiveMethod(n))
    # print(solution.bitwiseNaive(n))
    # print(solution.brain_kerningam(n))

    print(solution.lookupTable(n))