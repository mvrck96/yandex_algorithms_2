# Memory limit exceeded
n = int(input())
inp = []
flag = True
options = set(range(n))
yes_answers = []
no_answers = []

while flag:
    i = input()
    if i == "HELP":
        flag = False
        break
    else:
        inp.append(i)

for i in range(len(inp)):
    if inp[i] == "NO":
        no_answers.append(list(map(int, inp[i - 1].split())))
    if inp[i] == "YES":
        yes_answers.append(list(map(int, inp[i - 1].split())))

print(*sorted(set.intersection(options, *yes_answers) - set.union(*map(set, no_answers)) if no_answers != [] else set.intersection(options, *yes_answers)))