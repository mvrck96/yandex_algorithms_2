with open("input.txt", "r") as f:
    list_ = list(map(int, f.readlines()))[:-1]

max_ = list_[0]
cnt = 0
for i in list_:
    if max_ == i:
        cnt += 1
    if i > max_:
        cnt = 1
        max_ = i
print(cnt)
