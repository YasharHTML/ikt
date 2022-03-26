sample = input("Enter: ")
be = input("From: ")
to = input("To: ")
i = len(be)
z = 0
new_s = ""
for i in range(len(sample)):
    if sample[i:i+len(be)] == be:
        new_s += sample[z:i] + to
        z = i + len(be)
new_s += sample[z:]
print("Result:", new_s)