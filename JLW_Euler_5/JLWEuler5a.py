#Project Euler problem 5
#
# 2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by
# all of the numbers from 1 to 20?

#ver 5a checks individual primes

limit = 20    #highest number to check x is divisible by.

x = 20    #number to test.
p = [1,2,3,5,7,11,13,17,19] # prime section, needs work, see end doc
m=[0 for n in range(limit)]
print (m)
checkallmods = 1    #sum of all mod results for x%1, x%2...
                    #if this is zero then x is divisible cleanly by all
                    #init set to 1 else while loop won't start!

while checkallmods != 0:
    #print ("testing number",x)
    for i in range(len(p)):
        #print( "checking divisible by",p[i])
        m[i] = (x%(p[i]))    #m is array of all mod tests
        #print("mod of",x,"div by",i,"is",m[i])
        #print ("m",m)
        

    checkallmods = sum(m)
    #print("sequence of mods tested, sum is",checkallmods)

    if checkallmods == 0:
        print ("smallest number cleanly divisble by \
        all numbers from 1 to ",limit,"is",x) 

    else:
        x += limit  #this is key, increment in 20s since the answer
                    #must be multiple of 20!


        
##TO OPTIMISE

# don't need to test all of i
# if a number isn't divisible by 10 then it won't be by 20?
#BUT it could be div by 10 and NOT 20, how to solve this?
#EDIT: Nothing to solve; if it's not divisible then we dont care about it...
#... whether it fails one division or all of them!
#
# primes are the right way forward, but needs some more work
# need to use prime code from prev exercise (or keep it as a separate prime
# finder module and import this
