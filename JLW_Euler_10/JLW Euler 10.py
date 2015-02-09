## Project Euler 10  JLW 21/01/15

'''Summation of primes
Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.'''

#strategy, use sieve of Eratosthenes
# whatever is left is prime, sum them all

import time

start = time.clock()

target = 2000000


##SIEVE CODE BEGINS

# list with indices representing numbers to sieve for primality
lst_all_numbers = [True] * (target)

## special case for zero and one - not primes
lst_all_numbers[0] = False
lst_all_numbers[1] = False

lst_is_prime = []

print(len(lst_all_numbers))

print(lst_all_numbers[3])
# find the non-primes
for i in range(2, target, 1):
    #print("i", i)
    
    m = 2

    n = i*m
    
    while (n < target):

        n = i*m #####<------------------

        #print("n",n)
        if (n < target): # need this since while loop won't stop if n = i*m
                         # within loop (<-----) exceeds limit for n

            lst_all_numbers[n] = False

        m= m+1

# find primes in list
#print("running primes for loop")
for index,item in enumerate(lst_all_numbers):
   # print("checking", j)

    if (item == True):
        #print("prime", index)

        lst_is_prime.append(index)
        


#sum primes

print("sum of primes below", target, " = ", sum(lst_is_prime))

end = time.clock()

print("elapsed time", end-start)
