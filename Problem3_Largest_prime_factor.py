'''
Problem 3: Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''

def check_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def find_prime_divisors(n):
    primes = []
    i = 2
    while i <= n:
        if n % i == 0:
            if check_prime(i):
                primes.append(i)
                n //= i
        i += 1
    return primes

print(find_prime_divisors(600851475143)[-1])
# 6857
