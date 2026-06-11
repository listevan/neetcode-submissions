class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = [[] for i in range(len(nums)+1)]

        d = {}
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
        
        for key, value in d.items():
            counts[value].append(key)
        
        res = []
        counter = len(counts) - 1
        remaining = k
        while remaining > 0:
            if len(counts[counter]) > remaining:
                res += counts[counter][:remaining]
                return res
            else:
                res += counts[counter]
                remaining -= len(counts[counter])
                counter -= 1
        
        return res


        
        
