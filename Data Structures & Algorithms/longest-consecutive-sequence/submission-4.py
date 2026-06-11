class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        def join(s, ra, rb):
            a_s = s[ra]
            s[ra] = rb
            s[rb] += a_s

        def root(s, i):
            root = i
            count = 0
            while root >= 0 and s[root] >= 0:
                root = s[root]
                count += 1
                if count == 5:
                    root = -1
                    # print("cooked")
            
            return root


        v2i = {}
        for i, num in enumerate(nums):
            v2i[num] = i
        
        s = [-1] * len(nums)
        for i, num in enumerate(nums):
            if v2i[num] != i:
                continue

            if num + 1 in v2i:
                # join
                r = root(s, i)
                par_root = root(s, v2i[num+1])
                join(s, r, par_root)
                # print(s, i, r, par_root)

        if not s:
            return 0
        return min(s) * -1