class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        newa = sorted(set(point[0] for point in points))
        maxp = 0
        print(newa)
        for i in range(1,len(newa)):
            t = newa[i] - newa[i-1]
            maxp = max(t,maxp)
        return maxp
