def subarray_sum(nums,target):
    dict1 = {0:-1}
    cur_sum = 0
    for i,val in enumerate(nums):
        cur_sum +=val
        if cur_sum - target in dict1:
            return [dict1[cur_sum-target]+1,i]
            
        dict1[val] = i
    return []




nums = [1, 2, 3, 4, 5]
target = 9
print ( subarray_sum(nums, target) )

nums = [-1, 2, 3, -4, 5]
target = 0
print ( subarray_sum(nums, target) )

nums = [2, 3, 4, 5, 6]
target = 3
print ( subarray_sum(nums, target) )

nums = []
target = 0
print ( subarray_sum(nums, target) )



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 3]
    [0, 3]
    [1, 1]
    []

"""
