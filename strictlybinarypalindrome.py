class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        nbin = bin(n)[2:]
        res = int(nbin[::-1],2)

        return True if res==nbin else False
        
