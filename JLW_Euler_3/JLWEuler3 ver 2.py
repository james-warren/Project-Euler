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


# compute all primes up to this amount, then test each one?
# any quicker methods?
import math

tgt = 600851475143
#print (int(math.sqrt(tgt)))

# double for loop - will be slow!
#  doing first for only up to sqrt is massive time saving

for i in range (2, int(math.sqrt(tgt))):

    #print( "examining", i)

    if (tgt%i == 0):  #check if i is afactor, if so, check if prime
        #print("found factor", i)

        o = int(tgt/i)       # find co-factor (must declare int, else it floats)

        #print("found cofactor", o)
        i_isprime = 1     # i and o are prime until proven otherwise
        o_isprime = 1
        j = 2
        k = 2

###critical edit needed here.  the minute isprime goes to false, then you want to
###quit the for loop, no need to keep checking

        while ((i_isprime ==1) and j in range (2, int(math.sqrt(i)))):
                #print("testing primality of i",i, "trial", j)
                if (i%j == 0): #test for "i" not-prime
                    i_isprime = 0
                j = j+1
        ##now if your factor "i" is prime, print it
        if (i_isprime == 1):
            print ("found prime factor", i)

        while ((o_isprime ==1) and k in range (2, int(math.sqrt(o)))):         
                #print("testing primality of o",o, "trial", k)
                if (o%k == 0): #test for co-factor "o" not-prime
                    o_isprime = 0
                k = k+1
                        
        ##now if your co-factor "o" is prime, print it
        if (o_isprime == 1):
            print ("found prime cofactor", o)

print ("finished!")
        
    
