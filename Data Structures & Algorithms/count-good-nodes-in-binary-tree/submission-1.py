# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        s = []
        s.append((root,-1000))
        count = 0
        
        while s:
            curr, currm = s.pop()
            if not curr:
                continue

            if curr.val >= currm:
                currm = curr.val
                count += 1
            
            s.append((curr.left, currm))
            s.append((curr.right, currm))
        return count
            