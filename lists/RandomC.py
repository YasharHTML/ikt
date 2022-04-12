import random
li = [random.randint(1,6) for i in range(10)]
print(li)

max_ = li[0]
for i in range(len(li)):
    if li[i] > max_:
        max_ = li[i] 
x = 0
for i in li:
    if i == max_:
        x += 1
# use russian words
print(f'В списке {x} чисел равных {max_}')