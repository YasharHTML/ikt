import random
li = [random.randint(-100, 100) for i in range(10)]
print(li)


k = 0
for i in li:
    if i > 0:
        k+=1

print("Количество элементов больше 0:", k)