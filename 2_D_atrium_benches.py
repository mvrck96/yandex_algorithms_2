# Не работает !
l, k = map(int, input().split())
blocks = list(map(int, input().split()))

cntr = l // 2
left, right = [], []
print(cntr)
for i in blocks:
    if i < cntr: # Нужна обработка случая когда центр 2.5 а блок стоит на 2
        left.append(abs(cntr - i))
    else:
        right.append(abs(cntr - i))
print(left, right)

left_b = left.index(min(left))
right_b = right.index(min(right))

print(blocks[left_b], blocks[len(left) + right_b])
