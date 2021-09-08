str_ = input()

cnt = 0
if len(str_) % 2 == 0:
    if str_[len(str_) // 2 - 1 :: -1] == str_[len(str_) // 2 :]:
        print(0)
    else:
        for i, j in zip(str_[len(str_) // 2 - 1 :: -1], str_[len(str_) // 2 :]):
            if i != j:
                cnt += 1
        print(cnt)
else:
    if str_[:len(str_) // 2] == str_[:len(str_) // 2:-1]:
        print(0)
    else:
        for i, j in zip(str_[:len(str_) // 2], str_[:len(str_) // 2:-1]):
            if i != j:
                cnt += 1
        print(cnt)