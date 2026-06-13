class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        m = 0
        se = {}


        while r < len(s):
            if s[r] not in se or se[s[r]] < l:
                se[s[r]] = r
                m = max(r-l+1, m)
            else:
                l = se[s[r]] + 1
                se[s[r]] = r


            r += 1
        
        return m