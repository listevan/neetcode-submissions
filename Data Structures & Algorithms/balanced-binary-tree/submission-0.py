# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        s = [root]
        h = {None: 0}

        while s:
            c = s[-1]

            if c.left and c.left not in h:
                s.append(c.left)
            elif c.right and c.right not in h:
                s.append(c.right)
            else:
                s.pop()
                if abs(h[c.right] - h[c.left]) > 1:
                    return False
                h[c] = 1+max(h[c.right], h[c.left])
        
        return True
        