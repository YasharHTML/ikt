import random
li = [random.randint(1,6) for i in range(10)]
print(li)

print([li[-1]] + li[:-1])
