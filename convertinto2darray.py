class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        newa = []
        i = 0
        while nums:
            if nums[i] not in newa:
                newa.append(nums[i])
                nums.pop(i)
            else:
                i +=1

            if i>=len(nums):
                res.append(newa)
                newa = []
                i = 0
            

        return res
            

        
