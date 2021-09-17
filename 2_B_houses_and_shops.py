line = list(map(int, input().split()))
indexes_2, indexes_1 = [], []
max_ = 1

for i in range(len(line)):
    if line[i] == 1:
        indexes_1.append(i)
    elif line[i] == 2:
        indexes_2.append(i)

for i in indexes_1:
    dist_list = []
    for j in indexes_2:
        dist = abs(i - j)
        dist_list.append(dist)
    if min(dist_list) > max_:
        max_ = min(dist_list)
print(max_)
