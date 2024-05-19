class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        pos = []
        neg = []

        for i in nums:
            if i<0:
                neg.append(i)
            else:
                pos.append(i)
        newa = []
        for i,j in zip(pos,neg):
            newa.append(i)
            newa.append(j)
        return newa
