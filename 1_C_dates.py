x, y, z = map(int, input().split())

if x == y:
    res = 1
elif x <= 12 and y <= 12:
    res = 0
elif x > 12 and y <= 12:
    res = 1
elif x <= 12 and y > 12:
    res = 1
print(res)