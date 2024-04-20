class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max1 = 0
        for i in accounts:
            m1 = sum(i)
            if m1 > max1:
                max1 = m1
        return max1
