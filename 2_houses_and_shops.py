line = list(map(int, input().split()))

indexes_1 = [i for i, x in enumerate(line) if x == 1]
indexes_2 = [i for i, x in enumerate(line) if x == 2]
max_ = 1

for i in indexes_1:
    dist_list = []
    for j in indexes_2:
        dist = abs(i - j)
        dist_list.append(dist)
    if min(dist_list) > max_:
        max_ = min(dist_list)

print(max_)