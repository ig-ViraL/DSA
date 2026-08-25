# Easy problems

arr = [1, 2, 2, 3, 4, 4, 5]

def largestElement(arr):
    largest = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > largest:
            largest = arr[i]
    return largest

def secondLargestElement(arr):
    largest = second = float('-inf')
    for i in range(len(arr)):
        if arr[i] > largest:
            second = largest
            largest = arr[i]
        elif arr[i] > second and arr[i] != largest:
            second = arr[i]
    return second

def isSorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

def removeDuplicatesFromSortedArray(arr):
    if not arr:
        return arr
    write_index = 1
    for read_index in range(1, len(arr)):
        if arr[read_index] != arr[read_index - 1]:
            arr[write_index] = arr[read_index]
            write_index += 1
    arr = arr[:write_index]
    return arr

def rotate_array(arr, by, direction):
    print("Input Array : ", end=str(arr) + "\n")
    shifts = by % len(arr)
    print("Normalized Shift by :", str(shifts), direction)

    if direction == "right":
        arr.reverse()
        first_half = arr[:shifts]
        second_half = arr[shifts:]
        first_half.reverse()
        second_half.reverse()
        return first_half + second_half

    elif direction == "left":
        first_half = arr[:shifts]
        second_half = arr[shifts:]
        first_half.reverse()
        second_half.reverse()
        final_arr = first_half + second_half
        final_arr.reverse()
        return final_arr

    else:
        raise Exception(f"Invalid rotate direction ! Wtf is : {direction}")

# Medium problems

def twoSum(arr, target):
    num_map = {}
    for i, num in enumerate(arr):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []

arr = [0, 1, 2, 0, 1, 2]

def sort012():
    low = mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  # arr[mid] == 2
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr

arr = [1 ,0 ,2 ,3 ,0 ,4 ,0 ,1]

def move0ToEnd(arr):
    i = j = 0
    while j < len(arr):
        if arr[j] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        j += 1
    return arr

def findUniqueNumber(arr):
    seen = {}
    unique_numbers = {}
    for num in arr:
        if num not in seen:
            seen[num] = 1
            unique_numbers[num] = 1
        else:
            unique_numbers.pop(num, None)
    return list(unique_numbers.keys())[0] if unique_numbers else None

def longestSubarrayWithSumK(arr, k):
    longest_length = 0

    for i in range(len(arr)):
        current_sum = 0
        for j in range(i, len(arr)):
            current_sum += arr[j]
            if current_sum == k:
                longest_length = max(longest_length, j - i + 1)
    return longest_length

def longestSubarrayWithSumKOptimized(arr, k):
    longest_length = 0
    left = right = 0

    while right < len(arr):
        current_sum = sum(arr[left:right + 1])
        if current_sum < k:
            right += 1
        elif current_sum > k:
            left += 1
        else:
            longest_length = max(longest_length, right - left + 1)
            right += 1
    return longest_length

print(longestSubarrayWithSumK(arr, 3))