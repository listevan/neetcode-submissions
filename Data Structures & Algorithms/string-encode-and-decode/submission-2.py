class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += f"{len(s)}#{s}"
        return res
    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        l = ""
        found = False
        res = []
        cs = ""
        for i in range(len(s)):
            if l == 0:
                res.append(cs)
                l = ""
                cs = ""
                found = False
            print(i)
            if s[i] == "#" and not found:
                l = int(l)
                found = True
            elif not found:
                l += s[i]
            else:
                cs += s[i]
                l -= 1
        res.append(cs)
        return res
                
                