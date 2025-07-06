# ===== String Functions =====
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

def reverse_string(text):
    return text[::-1]

def is_palindrome(text):
    return text == text[::-1]


# ===== Math Functions =====
def add(a, b):
    return a + b

def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

def is_even(number):
    return number % 2 == 0


# ===== List Functions =====
def find_max(numbers):
    return max(numbers)

def find_min(numbers):
    return min(numbers)

def remove_duplicates(items):
    return list(set(items))
