class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        newa = []
        tot = 0
        for i in nums:
            tot +=i
            newa.append(tot)
        return newa
