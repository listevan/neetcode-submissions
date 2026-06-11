class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = set()
        for num in nums:
            if num in d:
                return True
            d.add(num)
        return False
        