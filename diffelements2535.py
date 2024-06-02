class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:

        t1 = sum(nums)
        t2 = 0
        for i in nums:
            
            while i!=0:
                temp = i%10
                t2 +=temp
                i = i//10

        return abs(t1-t2)


        
