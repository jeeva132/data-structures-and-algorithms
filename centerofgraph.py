class Solution:
    def findCenter(self, edge: List[List[int]]) -> int:
        return edge[0][0] if edge[0][0] == edge[1][0] or edge[0][0] == edge[1][1] else edge[0][1]
