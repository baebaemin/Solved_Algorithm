W, H = map(int, input().split())
l = (W+H) * 2
lst = [0] * l
N = int(input())
for _ in range(N+1):    # 둘레를 한 로 만들기 위한 idx 처리
    side, n = map(int, input().split())
    if side == 1: idx = l - n
    elif side == 2: idx = H + n
    elif side == 3: idx = n
    else: idx = l - (W + n)
    lst[idx] = 1

rlt = cnt = i = 0
while cnt < N:
    i += 1
    if lst[idx-i] == 1:
        cnt += 1
        rlt += i
        if i == l//2:  # 정반대편이라면 break
            break
    if lst[(idx+i)%l] == 1:
        cnt += 1
        rlt += i
        
print(rlt)