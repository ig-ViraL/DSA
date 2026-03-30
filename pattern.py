def pattern1(n):
    for i in range(n):
        for j in range(n):
            print('* ', end='')
        print('\n')

def pattern2(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print('* ', end='')
        print('\n')

def pattern3(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end='')
        print('\n')

def pattern4(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(i, end='')
        print('\n')

def pattern5(n):
    for i in range(1, n+1):
        for j in range(n, i-1, -1):
            print('*', end='')
        print('\n')

def pattern6(n):
    for i in range(1, n+1):
        for j in range(1, n - i + 1):
            print(' ', end='')
        for k in range(1, i * 2):
            print('*', end='')
        for l in range(1, n - i + 1):
            print(' ', end='')
        print('\n')

def pattern7(n):
    for i in range(1, n+1):
        for j in range(0, i):
            if(j > 0):
                print(' ', end='')
        for k in range(0, (n * 2) - (2 * i) + 1):
            print('*', end='')
        for l in range(0, i):
            if(j > 0):
                print(' ', end='')
        print('\n')

def pattern8(n):
    pattern6(n)
    pattern7(n)

def pattern9(n):
    for i in range(0, 2*n - 1):
        for j in range(0, i):
            print('*', end='')
        print('\n')

pattern9(5)