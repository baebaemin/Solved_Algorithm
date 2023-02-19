lst = [list(map(int, input().split())) for _ in range(3)]

def fourth(lst):
    if max(lst) == sorted(lst)[1]:
        return min(lst)
    else:
        return max(lst)

x_lst = []
y_lst = []
for i in range(3):
    x_lst.append(lst[i][0])
    y_lst.append(lst[i][1])

print(fourth(x_lst), fourth(y_lst))