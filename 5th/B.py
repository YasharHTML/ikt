import json

n = []
m = [21, 17, 15]
d = []
q = 0
l = 15
for i in range(l):
    for j in range(l):
        for k in range(l):
            z = [i, j, k]
            if z[0]*m[0] + z[1]*m[1] + z[2]*m[2] == 185:
                q += 1
                d += [{"Element": z}]
with open('test.json', 'w') as f:
    json.dump(d, f, ensure_ascii=True, indent=4, sort_keys=True)
print(q)
