import random
li = [random.randint(1,6) for i in range(10)]
# li = [1,2,3,4,5,6]
print(li)

print(li[0:len(li)//2][::-1] + li[len(li)//2:][::-1])