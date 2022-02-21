d, h, m, s = map(int, input("DD:HH:MM:SS -> ").split(':')) # input of time
print(d * 86400 + h * 3600 + m * 60 + s) # convert to seconds
