class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        d = abs(dividend)
        dv = abs(divisor)
        count = 0
        while d>=dv:
            temp = dv
            mul = 1
            while d >=temp:
                d -=temp
                count +=mul
                temp +=temp
                mul +=mul

        if (dividend<0 and divisor>=0) or (dividend>=0 and divisor <0):
            count = -count

        return min(2147483647,max(-2147483648,count))
        
