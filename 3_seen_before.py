l1 = list(map(int, input().split()))

seen = set() # Работа с множеством макс время на тестах 140 мс, работа с листом 2.08 секнды
for l in l1:
    if l in seen:
        print("YES")
    else:
        seen.add(l)
        print("NO")