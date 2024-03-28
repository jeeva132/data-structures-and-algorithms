# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # count = 0

        def dfs(cur):
            if cur is None:
                return 0
            
            return dfs(cur.left)+dfs(cur.right)+1
        return dfs(root)
        
        
