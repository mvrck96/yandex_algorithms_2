l1 = list(map(int, input().split()))

print(*list(filter(lambda x: l1.count(x) == 1, l1)))