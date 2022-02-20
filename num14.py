import random, math # import random and math modules
x, y = random.random(), random.random() # generate two random numbers between 0 and 1
print(round(math.sqrt(1 + y ** 2) * math.sin(x ** 2 / (1 + abs(y))), 3)) # print the result of the formula rounded to 3 decimal places