# JLW Project Euler Ex 9
"""Special Pythagorean triplet
Problem 9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc."""

from math import sqrt

# gettimg tactical

#ridiculous case of max c, 997 (for a<b<c and a = 1 b = 2)
#ERROR, can restrict more than this, 1,2,997 is not a right angled triangle
# and therefore will not obey Pythag. law

# since a <b <c
# a by definition must be < 334
# a**2 < 111556
# c2 < 223112
# c < 472 

# since a < b < c
# c > 334
# if c was less, you could not sum to 1000 without a or b being > c



a = 1
b = 1

for a in range(1, 334):

    
    for c in range ( 334, (1001-(2*a)) ):
        
        b = sqrt((c**2) - (a**2))

        if ((a + b + c) == 1000 ):

            print("Found pythag. triple tot 1000", a, b, c)
            print ("product is ", a*b*c)

            



    
    
