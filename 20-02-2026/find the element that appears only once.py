class Solution:
    def getSingleElement(self, arr):
        n = len(arr)
        for i in range(n):
            num = arr[i]
            count = 0
            for j in range(n):
                if arr[j] == num:
                    count += 1
            if count == 1:
                return num

        return -1  
arr = [4, 1, 2, 1, 2]
obj = Solution()
ans = obj.getSingleElement(arr)
print("The single element is:", ans)
