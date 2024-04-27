class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        i = 0
        j = n
        newa = []

        while i<=n-1:
            newa.append(nums[i])
            newa.append(nums[j])
            i +=1
            j +=1

        return newa


        
