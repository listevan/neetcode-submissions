# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        s = [(p, q)]
        while s:
            p_r, q_r = s[-1]
            s.pop()

            if p_r and q_r and p_r.val == q_r.val:
                s.append((p_r.left, q_r.left))
                s.append((p_r.right, q_r.right))
                continue
            if not p_r and not q_r:
                continue
            return False
        
        return True