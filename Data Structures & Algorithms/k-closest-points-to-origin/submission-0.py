class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []

        for p in points:
            d = -1*math.sqrt((p[0]-0)**2+(p[1]-0)**2)
            heapq.heappush(h, (d, p))
            while len(h) > k:
                heapq.heappop(h)
        
        return [v[1] for v in h]