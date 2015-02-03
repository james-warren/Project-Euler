# JLW Project Euler Ex 9
"""Special Pythagorean triplet
Problem 9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc."""

from math import sqrt

# gettimg tactical again

# a can't be bigger than b or c, so 1<a<333
# if a was bigger than this then b and c could not be larger than a
# 1000 without exceeding 

# smallest b will occur with biggest a
# so b must be at least 334
# b can't be bigger than 499 since then c can't be bigger than b
# with everything totalling 1000

#a+b+c must = 1000

# c = sqrt(a2 + b2)

# a + b + (sqrt(a2 + b2)) = 1000

# a + b = 1000 - sqrt (a2 + b2)

# a2 + b2 = 1000^2 - a2 - b2

# a2 + b2 = (1000 - a - b)*(1000 - a - b)

#a2 + b2 = 1000000 - 2000a - 2000b + a2 + b2 + 2ab

#0 = 1000000 - 2000(a+b) + 2ab # got this far without googling

# 0 = 500000 - 1000(a+b) + ab

# 0 = 500000 - 1000a - 1000b + ab

# 1000a -ab = 500000 - 1000b

#(1000 - b)*a = 500000 - 1000b

# a = (500000 - 1000b)/(1000 - b)

#general a = ((tgt^2/2) - tgt*b)/(tgt-b)

target = 1000

for b in range((int(target/3)),int(target/2)):

    a = ((target**2/2) - target*b)/(target - b)

    # if, supplying an integer b, a is an integer, then triplet found
    if (a%1 == 0):
        c = sqrt((a**2)+(b**2))
        print("triplet found, a,b,c", a, b, c)
        print("product abc", a*b*c)
    
