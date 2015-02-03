## JLW project Euler Ex 3  24/04/14
##
## The prime factors of 13195 are 5, 7, 13 and 29.
##
## What is the largest prime factor of the number 600851475143 ?

# factor must be a maximum of half the tgt
# (i.e. 2 * f = tgt)



# compute all primes up to this amount, then test each one?
# any quicker methods?

tgt = 600851475143

# double for loop - will be slow!
#  EDIT: Massively slow!
for i in range (2, int(tgt/2)):

## test for primality
    isprime = 1
    
    for j in range (2, i-1):
        if (i%j == 0):
            isprime = 0


    ##return is_prime = true (or false)
    if (isprime == 1):
        if (tgt%i == 0):
            print (i)

    ## can you do a C# style "if((isprime == true) && (tgt%i ==0))"
print ("finished!")
        
##### better method to try
##### guy on internet showed that sqrt(tgt) is largest you have to search
##### since if sqrt isnt factor then one factor must be less than sqrt!
##### you could then find the other larger factor using the small one
#
# so find all factors this way, then test only these for primality

