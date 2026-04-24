'''
    Difference is, as problem statement clearly states, arrays are sorted !
    So check for duplicates in same array for just last element ! that it !
    Because of sorting !
'''

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr2 = [2, 3, 4, 4, 5, 11, 12]

def union(arr, arr2):
    i = j = 0

    ans = []
    visited = {}

    while i < len(arr) and j < len(arr2):
        print(i, j)
        if arr[i] <= arr2[j]:
            if arr[i] not in visited:
                ans.append(arr[i])
                visited[arr[i]] = 1
            i += 1
        elif arr2[j] < arr[i]:
            if arr2[j] not in visited:
                ans.append(arr2[j])
                visited[arr2[j]] = 1
            j += 1
        else:  # equal
            if arr[i] not in visited:
                ans.append(arr[i])
                visited[arr[i]] = 1
            i += 1
            j += 1  # ✅ both increment
    
    while i < len(arr):
        if arr[i] not in visited:
            ans.append(arr[i])
            visited[arr[i]] = 1
        i += 1

    while j < len(arr2):
        if arr2[j] not in visited:
            ans.append(arr2[j])
            visited[arr2[j]] = 1
        j += 1

    return ans

def unionOptimized(arr, arr2):
    i = j = 0
    ans = []

    while i < len(arr) and j < len(arr2):
        if arr[i] < arr2[j]:
            if not ans or ans[-1] != arr[i]:
                ans.append(arr[i])
            i += 1
        elif arr2[j] < arr[i]:
            if not ans or ans[-1] != arr2[j]:
                ans.append(arr2[j])
            j += 1
        else:
            if not ans or ans[-1] != arr[i]:
                ans.append(arr[i])
            i += 1
            j += 1

    while i < len(arr):
        if not ans or ans[-1] != arr[i]:
            ans.append(arr[i])
        i += 1

    while j < len(arr2):
        if not ans or ans[-1] != arr2[j]:
            ans.append(arr2[j])
        j += 1

    return ans

print(union(arr, arr2))