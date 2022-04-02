def split_toDigits(n: str):
    n = str(n)
    return [int(x) for x in n]


n, p = map(int, input("n p> ").split())


def weird(n, p):
    k = split_toDigits(n)
    sum_ = 0
    for i in range(len(k)):
        sum_ += k[i] ** (p + i)
    if (sum_/n) % 1 == 0:
        return sum_ / n
    return None


print(int(weird(n, p)))
