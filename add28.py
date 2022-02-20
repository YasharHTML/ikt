minlimit = 50 # farenheit limit
minlimitspeed = 3 # mph limit
Ta, V = map(float, input("Ta, V -> ").split())  # input of temperature and wind speed in standard units
if Ta > minlimit and V > minlimitspeed:
    Ta = 1.8 * Ta + 32
    V = V * 1.6
    WCI = 13.12 + 0.6215*Ta - 11.37*(V**0.16) + 0.3965*Ta*(V**0.16)  # wind chill index using the formula from the assignment
    print("WCI = {}".format(round(WCI))) # print the wind chill index
else:
    print("Not valid") # print error message