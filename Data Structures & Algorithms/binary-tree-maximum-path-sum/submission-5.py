# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        s = [root]
        d = {None: float('-inf')}
        r = float('-inf')

        while s:
            c = s[-1]

            if c.left and c.left not in d:
                s.append(c.left)
            elif c.right and c.right not in d:
                s.append(c.right)
            else:
                s.pop()
                m = c.val
                r = max(r, c.val+d[c.left]+d[c.right])

                m = max(m, c.val+d[c.left])
                m = max(m, c.val+d[c.right])
                r = max(r, m)
                d[c] = m
                print(c.val, m)
        
        return r

# 8
# 9 -6
# null null 5 9
        