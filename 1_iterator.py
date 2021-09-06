task_res = int(input()) # int from -128 to 127
interactor = int(input()) # int from 0 to 7
checker = int(input()) # int from 0 to 7

if interactor == 0:
    if task_res != 0:
        res = 3
    else:
        res = checker
elif interactor == 1:
    res = checker
elif interactor == 4:
    if task_res != 0:
        res = 3
    else:
        res = 4
elif interactor == 6:
    res = 0
elif interactor == 7:
    res = 1
else:
    res = interactor
print(res)