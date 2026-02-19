def contains_duplicate(arr):
    seen = set()

    for x in arr:
        if x in seen:
            return True
        seen.add(x)

    return False


print(contains_duplicate([1,2,3,1]))
