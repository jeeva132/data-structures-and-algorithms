class Solution:
    def replaceDigits(self, s: str) -> str:

        stack = []

        for i in s:
            if i.isalpha():
                stack.append(i)
            else:
                stack.append(chr(ord(stack[-1])+int(i)))
        return ''.join(stack)
        
