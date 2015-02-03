## JLW project Euler Ex 3  24/04/14
##
## The prime factors of 13195 are 5, 7, 13 and 29.
##
## What is the largest prime factor of the number 600851475143 ?

# factor must be a maximum of half the tgt
# (i.e. 2 * f = tgt)

##### guy on internet http://www.mathblog.dk/project-euler-problem-3/
##### showed that sqrt(tgt) is largest you have to search
##### since if sqrt isnt factor then one factor must be less than sqrt!
##### you could then find the other larger factor using the sqrt
#
# so find all factors this way, then test only these for primality



import math

tgt = 600851475143

#print (int(math.sqrt(tgt)))

# double for loop - will be slow!
#  doing first for only up to sqrt is massive time saving

for i in range (2, int(math.sqrt(tgt) + 1)):

    # print( "examining", i)

    if (tgt%i == 0):  #check if i is afactor, if so, check if prime
        print("found factor", i)

        tgt = int(tgt/i)            # make new tgt e.g. if tgt 100, first factor is 2
        print ("New tgt is", tgt)   # now can have tgt 50 since cannot have any factors between 50 and 100


###critical edit needed here.  the minute isprime goes to false, then you want to
###quit the for loop, no need to keep checking
        i_isprime =1
        j = 2
        
        while ((i_isprime ==1) and j in range (2, int(math.sqrt(i) + 1))):
                print("testing primality of i",i, "trial", j)
                if (i%j == 0): #test for "i" not-prime
                    i_isprime = 0
                j = j+1
        ##now if your factor "i" is prime, print it
        if (i_isprime == 1):
            print ("found prime factor", i)

print ("finished!")

# really interesting, as ppl on net said, the factor finding method only ever finds primes
# so the actual primality check is redundant!
    
