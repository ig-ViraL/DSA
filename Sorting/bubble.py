# ╔═══════════════════════════════════════════════════════╗
# ║                   BUBBLE SORT                         ║
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

def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubbleSort([64, 25, 12, 22, 11]))