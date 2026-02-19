def find_missing(arr):
    n = len(arr) + 1
    expected = n * (n + 1) // 2
    actual = sum(arr)
    return expected - actual


print(find_missing([1,2,4,5]))
