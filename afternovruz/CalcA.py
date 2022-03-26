n = input("Enter a equation: ")
sum_ = 0
k = 0
t = 0
for i in range(len(n)):
    if n[i] == "+":
        sum_ += int(n[k:i])
        k = i + 1
        t = i
sum_ += int(n[t+1:])
print(sum_)