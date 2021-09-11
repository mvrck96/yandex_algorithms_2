l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

print(len(set(l1).intersection(set(l2))))