class Solution:
    def toLowerCase(self, s: str) -> str:
        lcase = ''
        for i in s:
            aval = ord(i)
            if 65<= aval <=90:
                lcase +=chr(aval+32)
            else:
                lcase +=i
        return lcase
