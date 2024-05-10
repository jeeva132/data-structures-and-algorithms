# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        def getval(val):
            return val if low<=val<=high else 0

        def dfs(root):
            if not root:
                return 0
            
            return getval(root.val)+dfs(root.left)+dfs(root.right)
            

            
        
        return dfs(root)
