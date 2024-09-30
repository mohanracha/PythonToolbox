import math

def psqrt(b):
    """Check if a number is a perfect square."""
    n = b
    a = int(n ** 0.5)
    return a * a == n

def even(a):
    """Check if a number is even."""
    return a % 2 == 0

def prime(a):
    """Check if a number is prime."""
    if a <= 1:
        return False
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            return False
    return True

def factors(a):
    """Return the factors of a number."""
    d = []
    for i in range(1, a + 1):
        if a % i == 0:
            d.append(i)
    print("Factors:", d)
    print("Count:", len(d))

def sumofeven(a, b):
    """Calculate the sum of even numbers between a and b."""
    s = 0
    for i in range(a, b + 1):
        if even(i):
            s += i
    print(s)

def sumofodd(a, b):
    """Calculate the sum of odd numbers between a and b."""
    s = 0
    for i in range(a, b + 1):
        if not even(i):
            s += i
    print(s)

def fact(a):
    """Calculate the factorial of a non-negative integer."""
    if a < 0:
        raise ValueError("Negative numbers do not have factorials.")
    result = 1
    for i in range(2, a + 1):
        result *= i
    return result

def fibo(a, b, n):
    """Return the nth Fibonacci number starting with a and b."""
    if n == 1:
        return a
    if n == 2:
        return b
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b

def palin(n):
    """Check if a number is a palindrome."""
    original = n
    reversed_num = 0
    while n > 0:
        last_digit = n % 10
        reversed_num = reversed_num * 10 + last_digit
        n //= 10
    return original == reversed_num

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32
