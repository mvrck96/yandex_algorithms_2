N, i, j = map(int, input().split())

if i > j:
    i, j = j, i
x1 = j - i - 1 
x2 = N - x1 - 2
res = min(x1, x2)
print(res)