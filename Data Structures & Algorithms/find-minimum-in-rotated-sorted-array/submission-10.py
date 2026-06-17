class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)
        res = -1

        while l < r:
            if nums[l] < nums[r-1]:
                return nums[l]

            m = (l + r - 1) // 2
            print(l,m,r)
            
            if nums[m] < nums[l]:
                res = m
                r = m + 1
            else:
                l = m+1
        
        return nums[res]