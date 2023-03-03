def paper(d_arr):
    global rlt
    for r in range(102):
        if sum(d_arr[r]) != 0:
            code = []
            for idx in range(101):
                if d_arr[r][idx] != d_arr[r][idx + 1]:
                    code.append(d_arr[r][idx])
            rlt += sum(code) * 2

N = int(input())
arr = [[0] * 102 for _ in range(102)]
for _ in range(N):
    N, M = map(int, input().split())
    for n in range(N, N+10):
        for m in range(M, M+10):
            arr[n][m] = 1

rlt = 0
paper(arr)
paper(list(zip(*arr)))
print(rlt)