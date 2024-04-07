class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ''

        carry = 0
        a,b = a[::-1],b[::-1]
        for i in range(max(len(a),len(b))):
            digitA = int(a[i]) if i<len(a) else 0
            digitB = int(b[i]) if i<len(b) else 0

            tot = digitA+digitB+carry
            char = str(tot%2)
            carry = tot//2
            res = char +res
        
        if carry:
            res = '1' + res
        return res
        
