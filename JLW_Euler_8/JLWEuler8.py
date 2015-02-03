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

### brute force (or iteration?)
# number of possible products is len of array minus len of prod
lst_of_products = [0]* ( len(inp_string)-num_adj_digits + 1)

highest_prod_numbers = []

for i in range( 0, (len(lst_of_products)) ):

    numbers_for_product = []

    
   # print("calculating product number", i+1)

    ###* this is weird.  It calcs Ok i.e. 13 numbers
    ### but surely range is e.g. ( 0, (0+13) )
    ### 0,1,2,3,4,5,6,7,8,9,10,11,12,13
    ### no, upper bound on range is not inclusive
    
    for j in range( i, (i + num_adj_digits) ):
       # print(j,"th number")

       # print("number included in product", inp_lst[j])

        numbers_for_product.append(inp_lst[j])    

    this_product = 1

    for item in numbers_for_product:

        this_product = this_product*item
        
    lst_of_products[i] = this_product

    if (max(lst_of_products) == lst_of_products[i]):

        highest_prod_numbers = numbers_for_product
        
    #print("product", i, "calculated", lst_of_products[i])

print(lst_of_products)

print(max(lst_of_products))

### need to state which numbers form this product
print(highest_prod_numbers)
