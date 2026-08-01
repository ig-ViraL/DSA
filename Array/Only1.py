# Find the number that appears once, and the other numbers twice

def only_one(arr):
    ans = None;
    dict = {}
    
    for i in arr:
        if(dict.get(i) == None):
            dict[i] = 1
            ans = i
        else:
            dict[i] += 1
            if(ans == i):
                ans = None
    return ans

print(only_one([1, 2, 3, 2, 1]))