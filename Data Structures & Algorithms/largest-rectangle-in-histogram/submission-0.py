class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s = []
        m = 0
        
        for r, height in enumerate(heights):
            l = r
            # print("r",r)
            while s and height < s[-1][1]:
                l, l_height = s.pop()
                # print(l, l_height)
                m = max(m, (r-l)*l_height)
            # print(l)
            s.append((l, height))

        while s:
            l, l_height = s.pop()
            m = max(m, (r-l+1)*l_height)

        return m