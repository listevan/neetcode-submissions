# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        s = [root]
        d = {None: 0}

        r = 0

        while s:
            c = s[-1]

            if c.left and c.left not in d:
                s.append(c.left)
            elif c.right and c.right not in d:
                s.append(c.right)
            else:
                s.pop()
                
                r = max(r, d[c.left] + d[c.right])
                d[c] = max(d[c.left], d[c.right]) + 1
        
        return r
        