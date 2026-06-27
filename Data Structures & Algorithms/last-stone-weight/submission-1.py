class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1*s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            if x != y:
                heapq.heappush(stones, -1*abs(x-y))
        if not stones:
            return 0
        return -1*stones[0]
        