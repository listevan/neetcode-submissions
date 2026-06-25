# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        q = deque([root])
        res = []
        while q:
            d = False
            lay = []
            for i in range(len(q)):
                c = q.popleft()
                if not c:
                    lay.append("null")
                    continue
                lay.append(str(c.val))
                d = True
                q.append(c.left)
                q.append(c.right)
            
            if d == False:
                break
            res.extend(lay)
        # print(",".join(res))
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        
        values = data.split(",")
        root = TreeNode(int(values[0])) if values[0] != "null" else None
        q = deque([root])
        
        i = 1
        while i < len(values):
            for j in range(len(q)):
                c = q.popleft()
                left = right = None
                if c:
                    left = c.left = TreeNode(int(values[i])) if values[i] != "null" else None
                    i += 1
                    right = c.right = TreeNode(int(values[i])) if values[i] != "null" else None
                    i += 1
                else:
                    i += 2
                if left:
                    q.append(left)
                if right:
                    q.append(right)
            
        return root
                
        