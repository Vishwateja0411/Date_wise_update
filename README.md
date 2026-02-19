# 17-02-2026

--

📘finding missing element in the array

🔹Approach (Sum Formula Method)

1.find n as:
    
    n=len(arr)+1

2.Calculate the expected sum using the formula.

    expected = n * (n + 1) // 2

3.Calculate the actual sum of elements in the array.

    actual = sum(arr)

4.The difference between expected sum and actual sum gives the missing number.

    expected - actual

--

--

📘Find Frequency of Each Element

🔹Approach (HashMap / Dictionary Method)

Use a dictionary to store element counts.

Traverse the array one by one.

For each element:

     If it already exists in the dictionary → increase its count.

     Otherwise → initialize count as 1.

Return the dictionary containing frequencies

🔹Steps

Create an empty dictionary freq.

Loop through each element in the array.

Update count using:

    freq[num] = freq.get(num, 0) + 1

Return the frequency dictionary.

--

--

📘Move Zeros to End

🔹Approach (Two Pointer Method)

Use two pointers:

    i → traverses the array

    j → points to the position where the next non-zero element should be placed

Traverse the array:

If the current element is non-zero:

    Swap it with the element at index j

    Increment j

After traversal, all non-zero elements will be at the beginning and zeros automatically move to the end.

🔹 Steps

Initialize pointer j = 0

Loop through the array using index i

If arr[i] != 0:

    Swap arr[i] and arr[j]

    Increment j

Return the modified array

--


--

📘 Sort Array of 0s, 1s, and 2s
🔹 Approach (Three Pointer Method)

Use three pointers:

    low → position where next 0 should go

    mid → current element being checked

    high → position where next 2 should go

Rules:

If element is 0:

    Swap with low

    Move both low and mid forward

If element is 1:

    Move mid forward

If element is 2:

    Swap with high

Move high backward (do not move mid immediately)

🔹 Steps

Initialize:
  
    low = 0
    mid = 0
    high = len(arr) - 1

Traverse while mid <= high

Apply rules based on value at arr[mid]

Return sorted array

--


# 18-02-2026

--

📘 Contains Duplicate

🔹 Approach (Set Method)

Use a set to store elements already seen.

Traverse the array one by one.

For each element:

        If it already exists in the set → duplicate found → return True.

        Otherwise, add it to the set.

If traversal completes without duplicates → return False.

🔹 Steps

Create an empty set seen

Loop through each element in the array

Check:

    If element exists in seen → return True

    Else add element to seen

Return False at the end

--

--

📘 Remove Duplicates from Sorted Array
🔹 Approach (Two Pointer Method)

Since the array is sorted, duplicates are adjacent.

Use two pointers:

    i → points to last unique element

    j → scans the array

Compare nums[j] with nums[i]:

    If different → found a new unique element

    Move i forward

    Replace nums[i] with nums[j]

Continue until the end

Return i + 1 (number of unique elements)

🔹 Steps

If array is empty → return 0

Initialize i = 0

Loop j from index 1 to end:

If nums[j] != nums[i]:

    Increment i

    Set nums[i] = nums[j]

Return i + 1

--

--

📘 Left Rotate Array by One Position

🔹 Approach (Shifting Method)

Store the first element in a temporary variable.

Shift all elements one position to the left.

Place the stored element at the last index.

🔹 Steps

Save first element:

    temp = nums[0]

Traverse from index 1 to end:

Shift each element left:

    nums[i-1] = nums[i]

Place temp at the last position:

    nums[-1] = temp
--
