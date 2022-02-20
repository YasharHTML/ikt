n = float(input("Enter in kilopascals: ")) # input of pressure
print("{} kilopascals is {} pounds per square inch".format(n, n * 0.145038)) # convert to pounds per square inch
print("{} kilopascals is {} millimeters of mercury".format(n, n * 7.50062)) # convert to millimeters of mercury
print("{} kilopascals is {} atmospheres".format(n, n * 0.00000986923266716)) # convert to atmospheres