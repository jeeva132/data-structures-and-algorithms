class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        pro = 1
        tot = 0

        while n:
            temp = n%10
            n = n//10
            pro *=temp
            tot +=temp
        return pro-tot
        
