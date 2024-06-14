class Solution:
    def countAsterisks(self, s: str) -> int:
        count ,t= 0,0
        for i in s:
            if i == '|':
                t +=1
            elif t%2 == 0:
                count +=i=='*'
        return count

        return count
        
