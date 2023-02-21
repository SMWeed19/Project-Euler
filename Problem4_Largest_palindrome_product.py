'''
Problem 4: Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''

def check_palindrome(n):
    str_n = str(n)
    midpoint = len(str_n) // 2
    for i in range(midpoint):
        if str_n[i] != str_n[-(i + 1)]:
            return False
    return True

product = 0
largest = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        product = i * j
        print(product)
        if check_palindrome(product):
            if product >= largest:
                largest = product

print(largest)
# 906609
