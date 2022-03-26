n = input("Enter equation:")
t = []
last_plus = 0
for i in range(len(n)):
    if n[i] == "+":
        t += [n[last_plus:i]]
        last_plus = i + 1
t += [n[last_plus:]]
sum = 0
for i in range(len(t)):
    sum += int(t[i])
print(sum)