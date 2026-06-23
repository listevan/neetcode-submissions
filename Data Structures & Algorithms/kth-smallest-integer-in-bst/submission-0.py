# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        s = [root]
        d = set([None])
        counter = 0

        while s:
            c = s[-1]
            if c.left and c.left not in d:
                d.add(c.left)
                s.append(c.left)
            else:
                s.pop()
                counter += 1
                if counter == k:
                    return c.val
                if c.right:
                    d.add(c.right)
                    s.append(c.right)

        