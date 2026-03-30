# ╔═══════════════════════════════════════════════════════╗
# ║                   MERGE SORT                          ║
# ╠═══════════════════════════════════════════════════════╣
# ║  Property          │  Value                           ║
# ╠════════════════════╪══════════════════════════════════╣
# ║  Time Complexity   │  O(n log n)                      ║
# ╠════════════════════╪══════════════════════════════════╣
# ║  Space Complexity  │  O(n)                            ║
# ╠════════════════════╪══════════════════════════════════╣
# ║  Stable            │  Yes                             ║
# ║  In-place          │  No                              ║
# ║  Online            │  No                              ║
# ║  Adaptive          │  No                              ║
# ╚════════════════════╧══════════════════════════════════╝

def merge_sort(arr):
    if(len(arr) <= 1):
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

test_arr = [64, 25, 12, 22, 11]
print(merge_sort(test_arr))