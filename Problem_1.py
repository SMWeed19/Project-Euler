# Problem 1: Multiples of 3 or 5

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6, and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def find_multiples(m, n):
    multiples_of_m_below_n = []
    for i in range(1, n):
        if i % m == 0:
            multiples_of_m_below_n.append(i)
    return multiples_of_m_below_n

three = find_multiples(3, 1000)
five = find_multiples(5, 1000)

sum = 0
for i in three:
    sum += i
for i in five:
    sum += i

print(sum)
