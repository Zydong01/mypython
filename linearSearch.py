
pos = 0
def search(lst, n):
    value = 0
    for i in lst:
        if i == n:
            value = 1
            break
        globals()['pos'] += 1
    return value

list = [1, 2, 3, 4]

if search(list, 4):
    print("有,在第{}位置".format(pos+1))
else:
    print("没有")
