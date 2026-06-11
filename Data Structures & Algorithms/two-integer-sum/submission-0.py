class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, num in enumerate(nums):
            d[num] = i
        
        res = []
        for i, num in enumerate(nums):
            if target - num in d and i != d[target-num]:
                res = [i, d[target-num]]
                break
        
        return res