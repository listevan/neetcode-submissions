class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        
        for stri in strs:
            count = [0]*26
            for l in stri:
                count[ord(l) - ord('a')] += 1
            
            if tuple(count) not in res:
                res[tuple(count)] = [stri]
            else:
                res[tuple(count)].append(stri)
        
        return list(res.values())

        