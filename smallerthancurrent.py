class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        newa = sorted(nums)
        res = [0 for i in range(len(nums))]
        for i in range(len(nums)):
            for j in newa:
                if j<nums[i]:
                    res[i]+=1
        return res
        
