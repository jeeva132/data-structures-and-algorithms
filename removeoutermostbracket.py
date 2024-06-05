class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count = 0
        res = ''
        for i in range(len(s)):
            if s[i] == '(':
                count +=1
                if count >1:
                    res +=s[i]
            elif s[i] == ')':
                count -=1
                if count >0:
                    res +=s[i]
        return res
        
