class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = ''
        indices = list(indices)

        for i in range(len(s)):
            temp = indices.index(i)
            res +=s[temp]
        
        return res
