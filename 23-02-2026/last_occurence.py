def solve(n: int, key: int, v: list[int]) -> int:
    res = -1
    for i in range(n - 1, -1, -1):
        if v[i] == key:
            res = i
            break
    return res

def main():
    n = 7
    key = 13
    v = [3, 4, 13, 13, 13, 20, 40]
    print(solve(n, key, v))


