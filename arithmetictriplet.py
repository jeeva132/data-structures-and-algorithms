class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        dict = {}
        for i in nums:
            dict[i] = dict.get(i,0) +1
        count = 0
        for i in nums:
            if dict.get(i+diff) and dict.get(i+diff*2):
                count +=1
        return count
