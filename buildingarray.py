class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        
        newa = []
        for i in range(len(nums)):
            newa.append(nums[nums[i]])

        return newa
