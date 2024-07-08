class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        diff = 0
        for i in set(s):
            ins = s.index(i)
            it = t.index(i)

            diff += abs(ins-it)
        return diff 
