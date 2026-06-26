class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.mh = []
        self.k = k

        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heapq.heappush(self.mh, val)
        while len(self.mh) > self.k:
            heapq.heappop(self.mh)
        
        return self.mh[0]
