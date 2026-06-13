class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        m = 0
        res = 0
        counts = {}

        while r < len(s):
            counts[s[r]] = 1 + counts.get(s[r], 0)
            m = max(m, counts[s[r]])

            while (r - l + 1) - m > k:
                counts[s[l]] -= 1
                l += 1

            res = max(res, r-l+1)
            r += 1
        
        return res
            