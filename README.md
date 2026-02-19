# 17-02-2026
1.finding missing element in the array

->Approach (Sum Formula Method)
find n as:
n=len(arr)+1
The sum of numbers from 1 to n is known:
n * (n + 1) / 2
Calculate the expected sum using the formula.
expected = n * (n + 1) // 2
Calculate the actual sum of elements in the array.
actual = sum(arr)
The difference between expected sum and actual sum gives the missing number.
expected - actual
