N = int(input())
cords = list(map(int, input().split()))

#А вот эторешение не проходит
point_sum = 0
sum_list = []
line = list(range(min(cords), max(cords)+1)) 

list_ = []
for i in line:
    list_.append((sum([abs(i - cord) for cord in cords])))
print(line[list_.index(min(list_))])

# Вот это решение проходит
print(cords[len(cords)//2])