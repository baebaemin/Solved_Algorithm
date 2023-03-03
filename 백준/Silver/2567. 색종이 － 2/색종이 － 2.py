N = int(input())
arr = [[0] * 102 for _ in range(102)]
for _ in range(N):
    N, M = map(int, input().split())
    for n in range(N, N+10):
        for m in range(M, M+10):
            arr[n][m] = 1

line = []
rlt = 0
for r in range(102):
    if sum(arr[r]) != 0:
        code = []
        if arr[r] == 1:
            rlt += 2
        for idx in range(101):
            if arr[r][idx] != arr[r][idx+1]:
                code.append(arr[r][idx])
        rlt += sum(code)*2

arr_t = list(zip(*arr))
for c in range(102):
    if sum(arr_t[c]) != 0:
        code = []
        for idx in range(101):
            if arr_t[c][idx] != arr_t[c][idx+1]:
                code.append(arr_t[c][idx])
        rlt += sum(code)*2
print(rlt)