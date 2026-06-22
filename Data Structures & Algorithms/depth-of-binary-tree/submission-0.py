# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        s = []
        s.append((root, 1))
        res = 0

        while s:
            curr, currh = s.pop()
            if not curr:
                continue
            
            res = max(res, currh)
            s.append((curr.left, currh+1))
            s.append((curr.right, currh+1))
        return res
        