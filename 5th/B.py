import json

n = []
m = [21, 17, 15]
d = []
q = 0
l = (9, 11, 13)
for i in range(l[0]):
    for j in range(l[1]):
        for k in range(l[2]):
            z = [i, j, k]
            if z[0]*m[0] + z[1]*m[1] + z[2]*m[2] == 185:
                q += 1
                d += [{"Element": z}]
with open('test.json', 'w') as f:
    json.dump(d, f, ensure_ascii=True, indent=4, sort_keys=True)
print(q)
