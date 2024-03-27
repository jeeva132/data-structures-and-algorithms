"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []

        def dfs(cur,res):
            if cur is None:
                return
            
            res.append(cur.val)
            for child in cur.children:
                dfs(child,res)
        

        dfs(root,res)
        return res
        
