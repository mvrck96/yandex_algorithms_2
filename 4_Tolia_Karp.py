n = int(input())
parcels = []

for i in range(n):
    parcels.append(tuple(map(int, input().split())))

res = dict.fromkeys([p[0] for p in parcels], 0)

for p in parcels:
    res[p[0]] += p[1]

for k in sorted(res.keys()):
    print(k, res[k])

