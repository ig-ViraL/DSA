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


print(removeDuplicatesFromSortedArray(arr))

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

print(sort012())