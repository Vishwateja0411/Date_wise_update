def find_median(nums1, nums2):
    merged = sorted(nums1 + nums2)
    n = len(merged)

    if n % 2 == 1:
        return merged[n // 2]
    else:
        return (merged[n//2 - 1] + merged[n//2]) / 2


print(find_median([1,3], [2]))
