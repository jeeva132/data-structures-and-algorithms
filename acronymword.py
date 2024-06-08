class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        res = []
        for i in words:
            if i:
                res.append(i[0])
        res = ''.join(res)

        if res == s:
            return True
        return False
        
