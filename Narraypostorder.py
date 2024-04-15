"""

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []

        def dfs(cur,res):
            if cur is None:
                return 
            
            for child in cur.children:
                dfs(child,res)
            res.append(cur.val)
        dfs(root,res)
        return res
        
