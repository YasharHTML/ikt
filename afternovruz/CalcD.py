import sys
n = input("Enter a equation: ")
sum_ = 0
new_s = ""
k = 0
par = [0, 0]
li = []
flag = True if ("*" not in n) and ("/" not in n) else False

if "/0" in n:
    sys.exit("Error: Division by zero")

for i in range(len(n)):
    if n[i] == "(":
        par[0] += i
    if n[i] == ")":
        par[1] += i
q = 0

for i in range(par[0]+1, par[1]):
    if "+" in n[par[0]+1: par[1]]:
        q = int(n[par[0]+1: par[1]].split("+")[0]) + int(n[par[0]+1: par[1]].split("+")[1])
    elif "-" in n[par[0]+1: par[1]]:
        q = int(n[par[0]+1: par[1]].split("-")[0]) - int(n[par[0]+1: par[1]].split("-")[1])
    elif "*" in n[par[0]+1: par[1]]:
        q = int(n[par[0]+1: par[1]].split("*")[0]) * int(n[par[0]+1: par[1]].split("*")[1])
    elif "/" in n[par[0]+1: par[1]]:
        q = int(n[par[0]+1: par[1]].split("/")[0]) // int(n[par[0]+1: par[1]].split("/")[1])
n = n[:par[0]] + str(q) + n[par[1] + 1:]

if flag:
    sum_ = 0
    new_s = ""
    for i in range(len(n)):
        if n[i] == "-":
            new_s += "+"
        new_s += n[i]
    for i in new_s.split("+"):
        sum_ += int(i)
    print(sum_)
    sys.exit("Done!")

for i in range(len(n)):
    if n[i] in ["+", "-"] and n[i-1] not in ["*", "/"]:
        li += [n[k:i]]
        li += [n[i]]
        k = i + 1

li += [n[k:]]
for i in range(len(li)):
    count_of_p = 0
    count_of_d = 0
    for l in li[i]:
        if l == "*":
            count_of_p += 1
        if l == "/":
            count_of_d += 1
    if not (count_of_p > 1 or count_of_d > 1):
        if "*" in li[i] or "/" in li[i]:
            z = li[i]
            if ("/" not in z) and ("*" in z):
                z = z.split("*")
                li[i] = str(int(z[0]) * int(z[1]))
            if ("/" in z) and ("*" not in z):
                z = z.split("/")
                li[i] = str(int(z[0]) // int(z[1]))
            if ("/" in z) and ("*" in z):
                m = []
                h = 0
                for j in range(len(z)):
                    if z[j] in ["*", "/"]:
                        m += [n[h:j]]
                        m += [n[j]]
                        h = j + 1
                m += [n[h:]]
                if m[1] == "*":
                    li[i] = str(int(m[0]) * int(m[2]) // int(m[4]))
                if m[1] == "/":
                    li[i] = str(int(m[0]) // int(m[2]) * int(m[4]))
                print(li[i])
                sys.exit("Done!")
    else:
        if "*" in li[i]:
            z = li[i].split("*")
            li[i] = str(int(z[0]) * int(z[1]) * int(z[2]))
        if "/" in li[i]:
            z = li[i].split("/")
            li[i] = str(int(z[0]) // int(z[1]) // int(z[2]))
        print(li[i])
        sys.exit("Done!")
        
if not flag:
    if "+" in li:
        print(int(li[0]) + int(li[2]))
    if "-" in li:
        print(int(li[0]) - int(li[2]))
    sys.exit("Done!")

if "+" in li:
    print(int(li[0]) + int(li[2]))
    sys.exit("Done!")
if "-" in li:
    print(int(li[0]) - int(li[2]))
    sys.exit("Done!")