n = input("Enter a equation: ")
sum_ = 0
new_s = ""

for i in range(len(n)):
    if n[i] == "-":
        new_s += "+"
    new_s += n[i]
for i in new_s.split("+"):
    sum_ += int(i)
print(sum_)