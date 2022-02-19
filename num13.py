import random
n = random.randint(10000,99999)
t = []
for i in range(0,5):
    print(n%10**2)
    n = n//10