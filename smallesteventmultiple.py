class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n%2 == 0:
            return n
        else:
            t = n+n
            return t
