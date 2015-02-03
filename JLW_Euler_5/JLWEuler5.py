#Project Euler problem 5
#
# 2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by
# all of the numbers from 1 to 20?

limit = 20    #highest number to check x is divisible by.

x = 20    #number to test.
m=[0 for n in range(limit)]
print (m)
checkallmods = 1    #sum of all mod results for x%1, x%2...
                    #if this is zero then x is divisible cleanly by all

while checkallmods != 0:
    #print ("testing number",x)
    for i in range(1,limit,1):
        #print( "checking divisible by",i)
        m[i] = (x%i)    #m is array of all mod tests
        #print("mod of",x,"div by",i,"is",m[i])
        #print ("m",m)
        

    checkallmods = sum(m)
    #print("sequence of mods tested, sum is",checkallmods)

    if checkallmods == 0:
        print ("smallest number cleanly divisble by \
        all numbers from 1 to ",limit,"is",x) 

    else:
        x += limit


        
##TO OPTIMISE

# don't need to test all of i
# if a number isn't divisible by 10 then it won't be by 20

#could code this manually i.e. test 2,3,5,7,11... infact all primes <20.
#the loop would be faster i.e. test 2,3,5,7,11,13,17,19 8 numbers not 20!
#BUT it could be div by 10 and NOT 20, how to solve this?



# perhaps use breakout characters in string i.e.
#print ("the list contains %s and %s and %s", %(1,2,3,))
