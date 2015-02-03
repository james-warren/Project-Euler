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


for a in range(1, 334):
  
    for b in range(334, 500):

        c = 1000 - (a + b)

        print("a, b, c", a, b, c)
        print("a^2", a**2, "b^2", b**2)
        print("c^2", c**2)
        print("a^2 + b^2", (a**2 + b**2))
        print("diff in sq = ", ( (c**2) - (a**2 + b**2) ))

        if ( ((a**2) + (b**2)) == (c**2) ):

            print("Found pythag. triple tot 1000", a, b, c)
            print ("product is ", a*b*c)

            



    
    
