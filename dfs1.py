class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    res = []

    def dfs(cur,res):
      if cur is None:
        return

      res.append(cur.value)
      dfs(cur.left,res)
      dfs(cur.right,res)
  dfs(root,res)
  return res
