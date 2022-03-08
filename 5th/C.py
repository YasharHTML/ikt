n = int(input("Enter: "))
t = [*range(1, n+1)]


def gR38(n, d) :
    return (d != 0 and n % d == 0)

def Pw21T_( n) :
    temp = n
    while (temp > 0):
        digit = temp % 10
        if ((gR38(n, digit)) == False) :
            return False
        temp = temp // 10
    return True

new_t = []
for i in t:
    if (Pw21T_(i)):
        new_t += [i]
print(new_t)