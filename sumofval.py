class Solution:
    def minimumSum(self, num: int) -> int:

        n = []
        while num:
            n.append(num%10)
            n = n//10

        n.sort()
        n1 = n[0]*10 + n[-1]
        n2 = n[1]*10+n[-2]
        return n1+n2
