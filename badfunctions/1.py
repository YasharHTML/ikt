def summer(*a):
    sum_ = 0
    for i in a:
        sum_ += i
    return sum_ % 2 == 0
    

n = int(input("> "))
li = []
li += [n]
while True:
    n = int(input("> "))
    if n == -1:
        break
    li += [n]
print("Even" if summer(*li) else "Odd")