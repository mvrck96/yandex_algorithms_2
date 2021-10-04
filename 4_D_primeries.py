# Подход к решению
parties = {}
with open("input.txt", "r") as f:
    lines = list(map(lambda x: x.split(), f.readlines()))
    for l in lines:
        parties[" ".join(l[:-1])] = int(l[-1])

all = sum(parties.values())
izb = all / 450

print(f"all - {all}, izb -- {izb}")

for partie, points in parties.items():
    print(f"{partie} -- {points // izb}")
