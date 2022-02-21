import random
t = []

while len(t) != 10:
    x = random.randint(1, 10000000)
    if x % 2 == 0:
        t += [x]    
print(len(t))