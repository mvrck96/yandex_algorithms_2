from itertools import chain

with open("input.txt", "r") as f:
    lines = list(map(lambda x: x.strip().split(), f.readlines()))
    lines = list(chain(*lines))

ans = []
for w in lines:
    if (lines.count(w), w) not in ans:
        ans.append((lines.count(w), w))

print(sorted(ans, key=lambda x: (x[0], str(x[1]))))
# Надо сделать лексиграфический обратный порядок для 2 элементов