import random # import random module

x = random.randint(1000,9999) # generate a random number between 1000 and 9999
t = [] # create an empty list
for i in range(0,4): # loop 4 times
    t += [x%10] # add the last digit of x to the list
    x = x//10 # remove the last digit of x
p = 1 # create a variable p
for i in t: # loop 4 times
    print(i ** 2) # print the square of the last digit of x
    p *= i # multiply p by the last digit of x
print(p) # print p