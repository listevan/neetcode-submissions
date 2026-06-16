import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        k = -1
        
        while l <= r:
            m = (l + r) // 2
            
            t = 0.0
            for i in range(len(piles)):
                t += math.ceil(piles[i] / float(m))

            if t > h:
                l = m+1
            elif t <= h:
                k = m
                r = m-1
        
        return k