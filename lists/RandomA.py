import random
li = [random.randint(1,6) for i in range(10)]
print(li)
max_ = li[0]
max_idx = 0
for i in range(len(li)):
    if li[i] > max_:
        max_ = li[i]
        max_idx = i

min_ = li[0]
min_idx = 0
for i in range(len(li)):
    if li[i] < min_:
        min_ = li[i]
        min_idx = i

print(max_ , max_idx)
print(min_ , min_idx)

    
