# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        s = []
        s.append(root)
        while s:
            curr = s.pop()
            # print(curr.val)
            if (p.val >= curr.val and q.val <= curr.val) or (p.val <= curr.val and q.val >= curr.val):
                return curr
            elif p.val > curr.val and q.val > curr.val:
                s.append(curr.right)
            else:
                s.append(curr.left)
        
        return