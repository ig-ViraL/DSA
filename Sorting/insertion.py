# ╔═══════════════════════════════════════════════════════╗
# ║                   INSERTION SORT                      ║
# ╠═══════════════════════════════════════════════════════╣
# ║  Property          │  Value                           ║
# ╠════════════════════╪══════════════════════════════════╣
# ║  Time Complexity   │  O(n²)                           ║
# ╠════════════════════╪══════════════════════════════════╣
# ║  Space Complexity  │  O(1)                            ║
# ╠════════════════════╪══════════════════════════════════╣
# ║  Stable            │  Yes                             ║
# ║  In-place          │  Yes                             ║
# ║  Online            │  Yes                             ║
# ║  Adaptive          │  Yes                             ║
# ╚════════════════════╧══════════════════════════════════╝

def insertionSortSwap(arr):
    for i in range(len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]  # Swap: 3 writes
            else:
                break
    return arr

def insertionSortShift(arr):
    for i in range(1, len(arr)):
        key = arr[i]                      # Save the element to insert
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]           # Shift: 1 write per element
            j -= 1
        arr[j + 1] = key                  # Place key in correct position
    return arr

test_arr = [64, 25, 12, 22, 11]
print("Swap-based:", insertionSortSwap(test_arr.copy()))
print("Shift-based:", insertionSortShift(test_arr.copy()))