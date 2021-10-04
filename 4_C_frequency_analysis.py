words = {}
with open("input.txt", "r") as f:
    lines = list(map(lambda x: x.split(), f.readlines()))
    for l in lines:
        for w in l:
            words[w] = words.get(w, 0) + 1

ans = []
for w in words:
    ans.append((-words[w], w))
ans.sort()
for a in ans:
    print(a[1])

# ========================
# from itertools import chain
# from collections import Counter

# with open("input.txt", "r") as f:
#     words = Counter(list(chain(*map(lambda x: x.strip().split(), f.readlines()))))

# ans = []
# for w in words:
#     ans.append((-words[w], w))
# ans.sort()
# for a in ans:
#     print(a[1])
