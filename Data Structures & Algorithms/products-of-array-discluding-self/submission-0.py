class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = [1] * len(nums)
        s = [1] * len(nums)
        for i in range(0, len(nums)):
            if i == 0:
                p[i] = nums[i]
                s[len(nums) - i - 1] = nums[len(nums) - i - 1]
            else:
                p[i] = nums[i] * p[i-1]
                s[len(nums) - i - 1] = nums[len(nums) - i - 1] * s[len(nums) - i]
        
        res = [0] * len(nums)
        for i in range(0, len(nums)):
            if i == 0:
                res[i] = s[i+1]
            elif i == len(nums) - 1:
                res[i] = p[i-1]
            else:
                res[i] = s[i+1]*p[i-1]
        
        return res