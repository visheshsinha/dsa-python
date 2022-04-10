class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        
        cache = {0: 0}
        
        for num in arr:
            currentRemainder = ((num % k) + k) % k # To handle negative elements in array
            
            if currentRemainder in cache:
                cache[currentRemainder] += 1
            else:
                cache[currentRemainder] = 1
        
        if cache[0] % 2 == 0:
            del cache[0]
        else:
            return False
        
        for currentRemainder in range(1, k):
            
            if currentRemainder in cache:
                if k - currentRemainder == currentRemainder:
                    if cache[currentRemainder] % 2 == 0:
                        del cache[currentRemainder]
                    else:
                        return False
                else:
                    if k - currentRemainder in cache:
                        if cache[currentRemainder] == cache[k - currentRemainder]:
                            del cache[currentRemainder]
                            del cache[k - currentRemainder]
                        else:
                            return False
                    else:
                        return False
        
        return len(cache) == 0