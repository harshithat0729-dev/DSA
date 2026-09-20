# DSA Week 1 - Arrays
# Python Practice: 30 Array + Two Pointers Problems
# Beginner-friendly solutions

# 1. Traverse an array
arr = [10, 20, 30, 40, 50]
for x in arr:
    print(x)

# 2. Print elements with index
for i in range(len(arr)):
    print(i, arr[i])

# 3. Find sum of array
print("Sum:", sum(arr))

# 4. Count even and odd elements
arr = [10, 15, 20, 25, 30, 35]
even = odd = 0
for x in arr:
    if x % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even:", even, "Odd:", odd)

# 5. Count positive and negative elements
arr = [10, -5, 8, -2, 0, 7]
positive = negative = 0
for x in arr:
    if x > 0:
        positive += 1
    elif x < 0:
        negative += 1
print("Positive:", positive, "Negative:", negative)

# 6. Find maximum element
arr = [12, 45, 7, 89, 23]
print("Maximum:", max(arr))

# 7. Find minimum element
print("Minimum:", min(arr))

# 8. Linear search
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

print("Linear search index:", linear_search([10, 20, 30, 40], 30))

# 9. Check if array is sorted
def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

print("Sorted:", is_sorted([1, 2, 3, 4, 5]))

# 10. Reverse an array
arr = [1, 2, 3, 4, 5]
arr.reverse()
print("Reversed:", arr)

# 11. Insert at the end
arr = [10, 20, 30]
arr.append(40)
print("Insert at end:", arr)

# 12. Insert at a given position
arr = [10, 20, 40, 50]
arr.insert(2, 30)
print("Insert at position:", arr)

# 13. Delete last element
arr = [10, 20, 30, 40]
arr.pop()
print("Delete last:", arr)

# 14. Delete element at an index
arr = [10, 20, 30, 40, 50]
del arr[2]
print("Delete at index:", arr)

# 15. Update an element
arr = [10, 20, 30, 40]
arr[2] = 99
print("Updated:", arr)

# 16. Binary search in a sorted array
def binary_search(arr, key):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    return -1

print("Binary search index:", binary_search([10, 20, 30, 40, 50], 40))

# 17. Move zeros to end
def move_zeros(arr):
    pos = 0
    for x in arr:
        if x != 0:
            arr[pos] = x
            pos += 1
    while pos < len(arr):
        arr[pos] = 0
        pos += 1
    return arr

print("Move zeros:", move_zeros([0, 1, 0, 3, 12]))

# 18. Missing number 1..n
def missing_number(arr):
    n = len(arr) + 1
    return n * (n + 1) // 2 - sum(arr)

print("Missing number:", missing_number([1, 2, 4, 5]))

# 19. Remove duplicates from sorted array
def remove_duplicates(arr):
    if not arr:
        return []
    result = [arr[0]]
    for x in arr[1:]:
        if x != result[-1]:
            result.append(x)
    return result

print("Without duplicates:", remove_duplicates([1, 1, 2, 2, 3, 4, 4]))

# 20. Rotate array by K
def rotate_array(arr, k):
    k %= len(arr)
    return arr[-k:] + arr[:-k] if k else arr

print("Rotate by K:", rotate_array([1, 2, 3, 4, 5], 2))

# 21. Two Sum (HashMap)
def two_sum(arr, target):
    seen = {}
    for i, x in enumerate(arr):
        need = target - x
        if need in seen:
            return [seen[need], i]
        seen[x] = i
    return []

print("Two Sum:", two_sum([2, 7, 11, 15], 9))

# 22. Two Sum in sorted array - Two Pointers
def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        total = arr[left] + arr[right]
        if total == target:
            return [left, right]
        elif total < target:
            left += 1
        else:
            right -= 1
    return []

print("Two Sum sorted:", two_sum_sorted([1, 2, 4, 6, 8, 9], 10))

# 23. Reverse array in-place - Two Pointers
def reverse_two_pointer(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

print("Reverse with two pointers:", reverse_two_pointer([1, 2, 3, 4, 5]))

# 24. Check palindrome - Two Pointers
def is_palindrome(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        if arr[left] != arr[right]:
            return False
        left += 1
        right -= 1
    return True

print("Palindrome:", is_palindrome([1, 2, 3, 2, 1]))

# 25. Move zeros to end - Two Pointers
def move_zeros_two_pointer(arr):
    left = 0
    for right in range(len(arr)):
        if arr[right] != 0:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
    return arr

print("Move zeros with two pointers:", move_zeros_two_pointer([0, 1, 0, 3, 12]))

# 26. Remove duplicates from sorted array - Two Pointers
def remove_duplicates_two_pointer(arr):
    if not arr:
        return 0, []
    write = 1
    for read in range(1, len(arr)):
        if arr[read] != arr[read - 1]:
            arr[write] = arr[read]
            write += 1
    return write, arr[:write]

print("Remove duplicates with two pointers:",
      remove_duplicates_two_pointer([1, 1, 2, 2, 3, 3, 4]))

# 27. Container With Most Water - Two Pointers
def max_area(height):
    left, right = 0, len(height) - 1
    best = 0
    while left < right:
        area = min(height[left], height[right]) * (right - left)
        best = max(best, area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return best

print("Container with Most Water:", max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))

# 28. 3Sum - Two Pointers
def three_sum(nums):
    nums.sort()
    result = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return result

print("3Sum:", three_sum([-1, 0, 1, 2, -1, -4]))

# 29. Sort array of 0s and 1s - Two Pointers
def sort_zeros_ones(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        while left < right and arr[left] == 0:
            left += 1
        while left < right and arr[right] == 1:
            right -= 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    return arr

print("Sort 0s and 1s:", sort_zeros_ones([0, 1, 1, 0, 1, 0]))

# 30. Merge Two Sorted Arrays - Two Pointers
def merge_sorted_arrays(a, b):
    i = j = 0
    result = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result

print("Merged sorted arrays:", merge_sorted_arrays([1, 3, 5], [2, 4, 6]))

# End of DSA Week 1 practice
