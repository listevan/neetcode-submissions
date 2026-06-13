class Solution:
    def trap(self, height: List[int]) -> int:
        pre = [0] * len(height)
        suf = [0] * len(height)

        for i, h in enumerate(height):
            if i == 0:
                pre[0] = h
            elif h > pre[i-1]:
                pre[i] = h
            else:
                pre[i] = pre[i-1]
        
        for i in range(len(height)-1, -1, -1):
            h = height[i]
            if i == len(height)-1:
                suf[i] = h
            elif h > suf[i+1]:
                suf[i] = h
            else:
                suf[i] = suf[i+1]
        
        res = 0
        for i in range(len(height)):
            res += min(pre[i], suf[i]) - height[i]
        
        return res

        