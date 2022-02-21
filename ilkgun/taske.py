import math, random # import math and random modules
a, b = map(int, input("Enter two numbers (sep by colon)").split(",")) # input of two numbers
x,y = random.randint(a, b), random.randint(a, b) # generate two random numbers between a and b
print("your random numbers are {0} and {1}".format(x, y)) # print the two random numbers
if x > 0 and y > 0: # if both numbers are positive
    print("{0} + {1} = {2}".format(x, y, x + y)) # print the sum of the two numbers
    print("{0} - {1} = {2}".format(x, y, x - y)) # print the difference of the two numbers
    print("{0} / {1} = {2}".format(x, y, x // y)) # print the quotient of the two numbers
    print("{0} % {1} = {2}".format(x, y, x % y)) # print the remainder of the division of the two numbers
    print("log10({0})".format(x, math.log10(x))) # print the logarithm of the first number to the base 10
    print("{0} ** {1} = {2}".format(x, y, x ** y)) # print the first number to the power of the second number
    print("{0} * {1} = {2}".format(x, y, x * y)) # print the product of the two numbers
elif x > 0 and y < 0: # if the first number is positive and the second number is negative
    print("{0} + ({1}) = {2}".format(x, y, x + y)) # print the sum of the two numbers
    print("{0} - ({1}) = {2}".format(x, y, x - y)) # print the difference of the two numbers
    print("{0} / ({1}) = {2}".format(x, y, x // y)) # print the quotient of the two numbers
    print("{0} % ({1}) = {2}".format(x, y, x % y)) # print the remainder of the division of the two numbers
    print("log10({0})".format(x, math.log10(x))) # print the logarithm of the first number to the base 10
    print("{0} ** ({1}) = {2}".format(x, y, x ** y)) # print the first number to the power of the second number
    print("{0} * ({1}) = {2}".format(x, y, x * y)) # print the product of the two numbers
elif x < 0: # if the first number is negative
    print("try again next time") # print "try again next time"