class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
      # brute force approach(n^2)
        # count = 0

        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if i != j and nums[i]+nums[j] < target:
        #             count +=1

        # return count

      # nlogn approach
        nums.sort()
        l,r = 0,len(nums)-1
        pairs = 0

        while l<r:
            if nums[l]+nums[r] <target:
                pairs +=r-l
                l +=1
            else:
                r -=1
        return pairs
    
        
