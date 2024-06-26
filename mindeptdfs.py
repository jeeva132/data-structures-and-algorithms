# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # c = 0

        def dfs(root):
            if not root:
                return 0
            
            if root.left and not root.right:
                return 1+dfs(root.left)
            elif root.right and not root.left:
                return 1 + dfs(root.right)
            else:
                return 1 + min(dfs(root.left),dfs(root.right))
        
        return dfs(root)
        
