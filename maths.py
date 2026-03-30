import time

def countDigits(n):
    count = 0
    while n > 0:
        count += 1
        n = n // 10
    return count

def reverseNumber(n):
    reverse = 0
    while n > 0:
        reverse = reverse * 10 + n % 10
        n = n // 10
    return reverse

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return (a * b) // gcd(a, b)


def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def isPrimeOptimized(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1): # Square root of n is the largest factor of n
        if n % i == 0:
            return False
    return True

def isPalindrome(n):
    return n == reverseNumber(n)

def isPerfectNumber(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum == n

def isArmStrongNumber(n):
    sum = 0
    temp = n
    digitsCount = countDigits(n)
    while temp > 0:
        digit = temp % 10
        sum += digit ** digitsCount 
        temp = temp // 10
    return sum == n

def allDivisors(n):
    start = time.time()
    for i in range(1, n+1):
        if n % i == 0:
            print(i, end=' ')
    end = time.time()
    print(f"Time taken: {end - start} seconds")

def allDivisorsOptimized(n):
    start = time.time()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            print(i, end=' ')
            if i != n // i:
                print(n // i, end=' ')
    end = time.time()
    print(f"Time taken optimized: {end - start} seconds")

print(allDivisors(50000))
print(allDivisorsOptimized(50000))