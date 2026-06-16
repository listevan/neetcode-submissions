class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) 

        while l < r:
            m = (l+r-1)//2
            if target > nums[m]:
                l = m+1
            elif target < nums[m]:
                r = m
            else:
                return m
        
        return -1