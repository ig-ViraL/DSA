def pattern1(n):
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print('\n')
    return

def pattern2(n):
    for i in range(n):
        for j in range(i+1):
            print('*', end=" ")
        print('\n')
    return

def pattern3(n):
    for i in range(n):
        for j in range(i+1):
            print(j+1, end=" ")
        print('\n')
    return

def pattern4(n):
    for i in range(n):
        for j in range(i+1):
            print(i+1, end=" ")
        print('\n')
    return

def pattern5(n):
    for i in range(n):
        for j in range(n, i, -1):
            print('*', end=" ")
        print('\n')
    return

def pattern6(n):
    for i in range(n):
        num = 1
        for j in range(n, i, -1):
            print(num, end=" ")
            num += 1
        print('\n')
    return

def pattern7(n):
    for i in range(1, n+1):
        for _ in range(n-i):
            print(' ', end=" ")
        for _ in range(i*2-1):
            print('*', end=" ")
        for _ in range(n-i):
            print(' ', end=" ")
        print('\n')
    return

def pattern8(n):
    for i in range(n):
        stars = n * 2 - (i * 2 + 1)
        for _ in range(i):
            print(' ', end=" ")
        for _ in range(stars):
            print('*', end=" ")
        for _ in range(i):
            print(' ', end=" ")
        print('\n')
    return

def pattern9(n):
    pattern7(n)
    pattern8(n)
    return

def pattern10(n):
    pattern2(n)
    for i in range(1, n):
        for _ in range(0, n - i):
            print('*', end=" ")
        print('\n')
    return

def pattern11(n):
    for i in range(n):
        char = 1 if i % 2 == 0 else 0        
        for _ in range(i+1):
            print(char, end=" ")
            char = 1 if char == 0 else 0
        print('\n')
    return

def pattern12(n):
    for i in range(1, n+1):
        space = (n - i) * 2
        for j in range(1, i+1):
            print(j, end=" ")
        for _ in range(space):
            print(' ', end=" ")
        for k in range(i, 0, -1):
            print(k, end=" ")
        print('\n')
    return

def pattern13(n):
    num = 1
    for i in range(1, n+1):
        for _ in range(i):
            print(num, end=" ")
            num += 1
        print('\n')
    return

def pattern14(n):
    for i in range(1, n+1):
        for j in range(i):
            print(chr(65 + j), end=" ")
        print('\n')
    return

def pattern15(n):
    for i in range(1, n+1):
        for j in range(n-i+1):
            print(chr(65 + j), end=" ")
        print('\n')
    return

def pattern16(n):
    charIndex = 65
    for i in range(1, n+1):
        for _ in range(i):
            print(chr(charIndex), end=" ")
        charIndex += 1
        print('\n')
    return

def pattern17(n):
    for i in range(1, n+1):
        for _ in range(n-i):
            print(' ', end=" ")
        for j in range(i):
            print(chr(65 + j), end=" ")
        for k in range(i-1, 0, -1):
            print(chr(65 + (k-1)), end=" ")
        for _ in range(n-i):
            print(' ', end=" ")
        print('\n')
    return

def pattern18(n):
    for i in range(1, n+1):
        start = 65 + (n - i)
        for j in range(i):
            print(chr(start + j), end=" ")
        print('\n')
    return

def pattern19(n):
    for i in range(n):
        for _ in range(n-i):
            print('*', end=" ")
        for _ in range(i*2):
            print(' ', end=" ")
        for _ in range(n-i):
            print('*', end=" ")
        print('\n')
    for i in range(1, n+1):
        for _ in range(i):
            print('*', end=" ")
        for _ in range((n-i)*2):
            print(' ', end=" ")
        for _ in range(i):
            print('*', end=" ")
        print('\n')
    return

def pattern20(n):
    for i in range(n):
        for _ in range(i):
            print('*', end=" ")
        for _ in range((n-i)*2):
            print(' ', end=" ")
        for _ in range(i):
            print('*', end=" ")
        print('\n')
    for i in range(n):
        for _ in range(n-i):
            print('*', end=" ")
        for _ in range(i*2):
            print(' ', end=" ")
        for _ in range(n-i):
            print('*', end=" ")
        print('\n')
    return

def pattern21(n):
    for i in range(n):
        if i == 0 or i == n-1:
            for j in range(n):
                print('*', end=" ")
        else:
            for j in range(n):
                if j == 0 or j == n-1:
                    print('*', end=" ")
                else:
                    print(' ', end=" ")  
        print('\n')   
    return

def pattern22(n):
    size = 2 * n - 1
    center = n - 1
    for i in range(size):
        for j in range(size):
            print(max(abs(i - center), abs(j - center)) + 1, end=" ")
        print()
    return

pattern22(4)