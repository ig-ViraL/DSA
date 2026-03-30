def sumOfNumbers(n):
    if n == 0:
        return 0
    return n + sumOfNumbers(n-1)

def sumOfNumbersOptimized(n):
    return n * (n + 1) // 2

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(20))