# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        s = []
        s.append((root, -1001, 1001))
        
        while s:
            curr, l, r = s.pop()
            if not curr:
                continue
            if not (curr.val > l and curr.val < r):
                return False
            
            s.append((curr.left, l, curr.val))
            s.append((curr.right, curr.val, r))


        return True 