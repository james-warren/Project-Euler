'''Problem 8
The four adjacent digits in the 1000-digit number
that have the greatest product are 9 × 9 × 8 × 9 = 5832.

73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450

Find the thirteen adjacent digits in the 1000-digit
number that have the greatest product. What is the value of this product?'''

#### number received as string
inp_string = "73167176531330624919225119674426574742355349194934\
96983520312774506326239578318016984801869478851843\
85861560789112949495459501737958331952853208805511\
12540698747158523863050715693290963295227443043557\
66896648950445244523161731856403098711121722383113\
62229893423380308135336276614282806444486645238749\
30358907296290491560440772390713810515859307960866\
70172427121883998797908792274921901699720888093776\
65727333001053367881220235421809751254540594752243\
52584907711670556013604839586446706324415722155397\
53697817977846174064955149290862569321978468622482\
83972241375657056057490261407972968652414535100474\
82166370484403199890008895243450658541227588666881\
16427171479924442928230863465674813919123162824586\
17866458359124566529476545682848912883142607690042\
24219022671055626321111109370544217506941658960408\
07198403850962455444362981230987879927244284909188\
84580156166097919133875499200524063689912560717606\
05886116467109405077541002256983155200055935729725\
71636269561882670428252483600823257530420752963450"

print(inp_string)

###first get it into list form as integers

inp_lst = [0]*len(inp_string)

for index, value in enumerate(inp_string):

    inp_lst[index] = int(value)

print(inp_lst)

### now to calculate the products

# product of how many adjacent numbers?
num_adj_digits = 13

### try recursion
# number of possible products is len of array minus len of prod
lst_of_products = [0]* ( len(inp_string)-num_adj_digits + 1)

highest_prod_numbers = []

for i in range( 0, (len(lst_of_products)) ):

    # initial case - first product of 13 numbers
    if ( i == 0):
        print(i, "initial case")

        numbers_for_product = []

        for j in range( i, (i + num_adj_digits) ):

            numbers_for_product.append(inp_lst[j])

        this_product = 1

        for item in numbers_for_product:

            this_product = this_product*item
        
        lst_of_products[i] = this_product

        if ( (max(lst_of_products)) == (lst_of_products[i]) ):
            
            #highest_prod_numbers = numbers_for_product
            print("updating highest prod numbers - initial case")
            print("highest prod numbers", highest_prod_numbers)
            
        else:
            print("no new max - initial case")
            print("highest prod numbers", highest_prod_numbers)
            
    # all other cases
    else:
        print(i, "th case")
        print("hpn1", highest_prod_numbers)

        this_product = 1
        
        for k in range(0, (len(numbers_for_product)-1) ): #NOT for last one, since there is no k+1 for final k!
            numbers_for_product[k] = numbers_for_product[k+1] #shift list to left

        numbers_for_product[(len(numbers_for_product)-1)] = inp_lst[i+num_adj_digits-1] #add next item to end
        print("hpn2", highest_prod_numbers) #***this is where update  highest prod number error happens!!!

        ###### this is something to do with pass-by-reference/pointer/object etc.
        ###### in essence it seems that both the numbers_for_product
        ###### and highest_prod_numbers point to the same area in memory.
        ###### when this gets updated both things looking at it are affected.
        ###### BUT it may have something to do with "mutable" types (list is mutable).
        ###### for int or string it won't be the same (immutable)

        print(numbers_for_product)

        for item in numbers_for_product:

            this_product = this_product*item
        
        lst_of_products[i] = this_product
        print("hpn3", highest_prod_numbers)
        
        if ( max(lst_of_products) == lst_of_products[i] ):

            highest_prod_numbers = numbers_for_product
            print("updating highest prod numbers -", i,"th case")

            print("highest prod numbers", highest_prod_numbers)

        else:
            print("no new max", i,"th case")
            print("highest prod numbers", highest_prod_numbers)
        #* WHY IS THIS ALWAYS UPDATING?

print(lst_of_products)

print(max(lst_of_products))

print("highest_prod_numbers", highest_prod_numbers)
### need to state which numbers form this product *BUG this always seems to update to the last product, not max!!!
