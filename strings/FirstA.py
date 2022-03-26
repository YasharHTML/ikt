n = input("Enter: ")
new_n = ""
for i in n:
    if i == "a":
        print("b", end="")
    elif i == "b":
        print("a", end="")
    else:
        print(i, end="")