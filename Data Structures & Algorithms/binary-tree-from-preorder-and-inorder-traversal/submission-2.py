# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        d = {}
        for i, v in enumerate(inorder):
            d[v] = i
        
        self.i = 0
        def dfs(l, r):
            if self.i >= len(preorder):
                return None
            if r <= l:
                return None
            curr = TreeNode(preorder[self.i])
            split = d[preorder[self.i]]

            self.i+=1
            curr.left = dfs(l, split)
            curr.right = dfs(split+1, r)

            return curr

        return dfs(0, len(inorder))