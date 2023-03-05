W, H = map(int, input().split())
l = (W+H) * 2
lst = [0] * l
N = int(input())
for _ in range(N+1):
    side, n = map(int, input().split())
    if side == 1: idx = l - n
    elif side == 2: idx = H + n
    elif side == 3: idx = n;
    else: idx = l - (W + n)
    lst[idx] = 1
lst[idx] = 2
# print(lst, idx)
rlt = cnt = 0
i = 1
while cnt < N:
    if lst[idx-i] == 1:
        cnt += 1
        rlt += i
        if i == l//2:
            break
    if lst[(idx+i)%l] == 1:
        cnt += 1
        rlt += i
    i += 1
print(rlt)