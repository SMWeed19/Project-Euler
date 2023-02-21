'''
Problem 7: 10001st prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
'''

def check_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

i = 1
j = 2
while i < 10001:
    j += 1
    if check_prime(j):
        i += 1

print(j)
# 104743
