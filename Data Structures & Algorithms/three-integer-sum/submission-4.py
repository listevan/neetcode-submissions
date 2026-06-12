class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums = sorted(nums)

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = 0 - nums[i]

            l = i+1
            r = len(nums) - 1

            while l < r:
                if nums[l] + nums[r] == target:
                    # print(nums, i, l, r)
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l > 0 and l < len(nums) and nums[l] == nums[l-1]:
                        l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                    while r < len(nums)-1 and r >= 0 and nums[r] == nums[r+1]:
                        r -= 1
                else:
                    l += 1
                    while l > 0 and l < len(nums) and nums[l] == nums[l-1]:
                        l += 1

        return res