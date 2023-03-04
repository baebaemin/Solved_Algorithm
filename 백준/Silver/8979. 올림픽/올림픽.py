N, K = map(int, input().split())
lst = [0] * N
for i in range(N):
    n, G, S, B = map(int, input().split())
    lst[n-1] = (G*3 + S*2 + B*1, n*-1)
item, score = lst[K-1], lst[K-1][0]
lst = [(-1, 0)] + sorted(lst, reverse=True)
rlt = idx = lst.index(item)
cnt = 0
while 1:        # 앞에 동일 등수 국가가 있는지 찾기
    idx -= 1
    if lst[idx][0] != score:
        break
    cnt += 1
print(rlt - cnt)