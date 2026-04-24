# Find missing number :
# Find sum of array total, then n (n + 1) / 2 - total (Simple Maths - Series problem)


def find_missing_number(arr, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum


# Example
arr = [1, 2, 4, 5, 6]
n = 6

missing = find_missing_number(arr, n)
print(f"Array: {arr}")
print(f"Missing number: {missing}")
