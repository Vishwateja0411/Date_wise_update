class UpperBoundFinder:
    def upper_bound(self, arr, x):
        low, high = 0, len(arr) - 1
        ans = len(arr) 

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] > x:
                ans = mid   
                high = mid - 1
            else:
                low = mid + 1
        return ans

arr = [3, 5, 8, 9, 15, 19]
x = 9
finder = UpperBoundFinder()
ind = finder.upper_bound(arr, x)
print("The upper bound is the index:", ind)
