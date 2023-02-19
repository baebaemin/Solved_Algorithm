def dice(d_three, d_lst):
    if len(d_three) == 1:
        return 10000 + a * 1000
    elif len(d_three) == 3:
        return max(d_lst) * 100
    else:
        if max(d_lst) == sorted(d_lst)[1]:
            return 1000 + max(d_lst) * 100
        else:
            return 1000 + min(d_lst) * 100

rlt_lst = []
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    three = {a, b, c}
    lst = [a, b, c]
    rlt_lst.append(dice(three, lst))

print(max(rlt_lst))