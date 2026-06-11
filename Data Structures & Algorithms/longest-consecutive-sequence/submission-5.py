class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()
        for num in nums:
            s.add(num)
        longest = 0
        for num in s:
            if num-1 not in s:
                curr = num
                l=0
                while curr in s:
                    l += 1
                    curr += 1
                longest= max(longest, l)
        
        return longest