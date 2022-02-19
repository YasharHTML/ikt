import math, random
a, b = map(int, input("Enter two numbers (sep by colon)").split(","))
x,y = random.randint(a, b), random.randint(a, b)
print("your random numbers are {0} and {1}".format(x, y))
if x > 0 and y > 0:
    print("{0} + {1} = {2}".format(x, y, x + y))
    print("{0} - {1} = {2}".format(x, y, x - y))
    print("{0} / {1} = {2}".format(x, y, x // y))
    print("{0} % {1} = {2}".format(x, y, x % y))
    print("log10({0})".format(x, math.log10(x)))
    print("{0} ** {1} = {2}".format(x, y, x ** y))
    print("{0} * {1} = {2}".format(x, y, x * y))
elif x > 0 and y < 0:
    print("{0} + ({1}) = {2}".format(x, y, x + y))
    print("{0} - ({1}) = {2}".format(x, y, x - y))
    print("{0} / ({1}) = {2}".format(x, y, x // y))
    print("{0} % ({1}) = {2}".format(x, y, x % y))
    print("log10({0})".format(x, math.log10(x)))
    print("{0} ** ({1}) = {2}".format(x, y, x ** y))
    print("{0} * ({1}) = {2}".format(x, y, x * y))
elif x < 0:
    print("try again next time")