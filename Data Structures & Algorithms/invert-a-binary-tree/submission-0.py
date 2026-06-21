# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        s = []
        s.append(root)
        while s:
            curr = s.pop()
            if not curr:
                continue
            else:
                curr.left, curr.right = curr.right, curr.left
                s.append(curr.left)
                s.append(curr.right)
            
        return root