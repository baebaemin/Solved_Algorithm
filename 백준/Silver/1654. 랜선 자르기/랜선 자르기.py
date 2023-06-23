K, N = map(int, input().split())
lst = [int(input()) for _ in range(K)]


def divider(s, m, e):  # 1, 229, 457
    if (e - s) <= 1:
        cut_s = cut_e = 0
        for i in range(K):
            cut_s += lst[i] // s
            cut_e += lst[i] // e
        if cut_s > cut_e:
            return s
        else:
            return e

    cut = 0
    for i in range(K):
        cut += lst[i] // m

    if cut >= N:
        s = m
        m = (m + e) // 2
    else:
        e = m
        m = (s + m) // 2
    return divider(s, m, e)


ep = max(lst)
cnt = 0
for i in range(K):
    cnt += lst[i] // ep
if cnt >= N:
    print(ep)
else:
    mp = (ep + 1) // 2
    print(divider(1, mp, ep))