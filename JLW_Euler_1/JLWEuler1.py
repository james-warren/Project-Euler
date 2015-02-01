##JLW Project Euler Ex 1   23/04/14


##If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
##The sum of these multiples is 23.

##Find the sum of all the multiples of 3 or 5 below 1000.

total = 0

for n in range (1, 1000):

    if n%3 == 0:
        print (n)
        total = total + n

    elif n%5 == 0:
        print (n)
        total = total + n

print("Total is", total)
##seems to work OK

