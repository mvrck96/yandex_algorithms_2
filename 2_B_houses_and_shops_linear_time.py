line = list(map(int, input().split()))
dist = [0] * len(line)
shop = -1000
for i in range(len(line)):
    if line[i] == 2:
        shop = i
    if line[i] == 1:
        dist[i] = i - shop
shop = 1000
ans = 0
for i in range(len(line) - 1, -1, -1):
    if line[i] == 2:
        shop = i
    if line[i] == 1:
        mindist = min(shop - i, dist[i])
        ans = max(ans, mindist)
print(ans)
