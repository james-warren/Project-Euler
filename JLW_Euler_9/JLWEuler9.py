# JLW Project Euler Ex 9
"""Special Pythagorean triplet
Problem 9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc."""

from math import sqrt

# brute force


finished = False

a = 1
b = 1

while ( finished == False ):

    tot_1k_or_greater = False

    b = a

    while ( tot_1k_or_greater == False ):

        c = ( sqrt( (a*a) + (b*b) ))

        #print("a", a, "b", b, "c", c)

        if ( (a + b + c) == 1000 ): # case when you have found tripleyt
            print ("Found pythag. triplet tot 1000:", a, b, c)
            print ("product is ", a*b*c)
        

            tot_1k_or_greater = True
            finished = True

        else: # all other cases

            if ( (a+b+c) > 1000 ): # exceeds 1k, start with new a,b
                tot_1k_or_greater = True

            else:   # still less than 1k, increment b
                b = b+1

    a = a+1
