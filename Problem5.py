'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

def lowest_common_denominator(m, n):
    prime_factorization_m = []
    prime_factorization_n = []
    prime_factorization_lcd = []
    lcd = 1
    while m > 1:
        for i in range(2, m + 1):
            if m % i == 0:
                prime_factorization_m.append(i)
                m = m // i
                break
    while n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                prime_factorization_n.append(i)
                n = n // i
                break
    for i in prime_factorization_m:
        prime_factorization_lcd.append(i)
        if i in prime_factorization_n:
            prime_factorization_n.remove(i)
    for i in prime_factorization_n:
        prime_factorization_lcd.append(i)
    for i in prime_factorization_lcd:
        lcd = lcd * i
    return lcd

lcd = lowest_common_denominator(2, 3)
for i in range (4, 21):
    lcd = lowest_common_denominator(i, lcd)

print(lcd)
# 232792560
