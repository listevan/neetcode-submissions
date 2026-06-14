class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_chars, s_chars = {}, {}
        for i in range(len(t)):
            t_chars[t[i]] = 1 + t_chars.get(t[i], 0)
        
        l, r = 0, 0
        min_str = ""
        have, need = 0, len(t_chars)
        while r < len(s):
            if s[r] in t_chars:
                s_chars[s[r]] = 1 + s_chars.get(s[r], 0)
                if s_chars[s[r]] == t_chars[s[r]]:
                    have += 1
            while have == need:
                if (r-l) < len(min_str) or min_str == "":
                    min_str = s[l:r+1]
                if s[l] in t_chars:
                    s_chars[s[l]] -= 1
                    if s_chars[s[l]] < t_chars[s[l]]:
                        have -= 1
                l += 1
            while l < len(s) and s[l] not in t_chars:
                l += 1

            r += 1

        return min_str