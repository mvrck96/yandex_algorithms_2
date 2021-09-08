flag = True
list_ = []
while flag:
    i = int(input())
    list_.append(i)
    if i == 0:
        flag = False
        
max_ = list_[0]
cnt = 0
for i in list_[:-1]:
    if max_ == i:
        cnt += 1
    if i > max_:
        cnt = 1
        max_ = i
print(cnt)