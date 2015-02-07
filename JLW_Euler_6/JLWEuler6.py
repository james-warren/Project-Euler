# Project Euler Ex 6 JLW
'''

The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

limit = 0

limit = int(input("Enter highest number e.g. 100 \n"))

# calc sum of squares

sum_of_squares = 0

i = 0

for i in range (1, limit, 1):

    this_square = i*i
    

    sum_of_squares = this_square + sum_of_squares
    print("i ", i, "sum of squares ", sum_of_squares)

print("sum of squares = ", sum_of_squares)

#calc sq of sum

sum_of_numbers = 0

for i in range (1, limit, 1):

    sum_of_numbers = i + sum_of_numbers
    print("i ", i, "sum of numbers ", sum_of_numbers)

big_square = (sum_of_numbers * sum_of_numbers)
print("square of sum = ", big_square)

# calc difference

difference = big_square - sum_of_squares

print("difference = ", difference)
    
    

