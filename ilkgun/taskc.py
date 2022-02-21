n = int(input("Dordreqemli ededin reqemlerini cemini ve hasilini tapmaq\nDordreqemli tam ededi daxil edin-> "))
a = n % 10
b = n // 10 % 10
c = n // 100 % 10
d = n // 1000
print("Ededin reqemleri: {0} {1} {2} {3}\nReqemleri cemi: {0} + {1} + {2} + {3} = {4}\nReqemleri hasili: {0} * {1} * {2} * {3} = {5}".format(d, c, b, a, a + b + c + d, a * b * c * d))