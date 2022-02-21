import random # import random module
n = random.randint(10000,99999) # generate a random number between 10000 and 99999
t = [] # create an empty list
for i in range(0,5): # loop 5 times
    print(n%10**2) # print the square of last digit of n
    n = n//10 # remove the last digit of n