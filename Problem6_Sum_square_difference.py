'''
Problem 6: Sum square difference

The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

def sum_of_squares(m, n):
    sum = 0
    for i in range(m, n + 1):
        sum += i * i
    return sum

def square_of_sum(m, n):
    sum = 0
    for i in range(m, n + 1):
        sum += i
    return sum * sum

print(square_of_sum(1,100) - sum_of_squares(1,100))
# 25164150
