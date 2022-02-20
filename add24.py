h, m, s = map(int, input("HH:MM:SS -> ").split(':')) # input of time
print(h * 3600 + m * 60 + s) # convert to seconds
