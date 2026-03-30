# ╔═══════════════════════════════════════════════════════╗
# ║                   SELECTION SORT                      ║
# ╠═══════════════════════════════════════════════════════╣
# ║  Property          │  Value                           ║
# ╠════════════════════╪══════════════════════════════════╣
# ║  Time Complexity   │  O(n²)                           ║
# ║  ├─ Best Case      │  O(n²)                           ║
# ║  ├─ Average Case   │  O(n²)                           ║
# ║  └─ Worst Case     │  O(n²)                           ║
# ╠════════════════════╪══════════════════════════════════╣
# ║  Space Complexity  │  O(1)                            ║
# ╠════════════════════╪══════════════════════════════════╣
# ║  Stable            │  No                              ║
# ║  In-place          │  Yes                             ║
# ║  Online            │  No                              ║
# ║  Adaptive          │  No                              ║
# ╚════════════════════╧══════════════════════════════════╝

def selectionSort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

print(selectionSort([64, 25, 12, 22, 11]))