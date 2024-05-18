class Solution:
    def balancedStringSplit(self, s: str) -> int:
        res = 0
        count = {
            "L":0,
            "R":0
        }

        for i in s:
            count[i] +=1

            if count['L'] == count['R']:
                res +=1
            
        return res
