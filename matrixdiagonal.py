class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum1 = 0

        for i in range(len(mat[0])):
            sum1 +=mat[i][i]

        n = len(mat)
        for i in range(n):
            sum1 +=mat[i][n-i-1]
        
        if n%2 == 1:
            sum1 -= mat[len(mat)//2][len(mat)//2]
        return sum1
        
