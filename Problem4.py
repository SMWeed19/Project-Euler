'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def check_palindrome(n):
    str_n = str(n)
    midpoint = len(str_n) // 2
    print(midpoint)
    for i in range(midpoint):
        print(str_n[i])
        print(str_n[-(i + 1)])
        if str_n[i] != str_n[-(i + 1)]:
            return False
    return True
