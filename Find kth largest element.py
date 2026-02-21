def find_kth_largest(nums, k):
    nums.sort()
    return nums[-k]


print(find_kth_largest([3,2,1,5,6,4], 2))
