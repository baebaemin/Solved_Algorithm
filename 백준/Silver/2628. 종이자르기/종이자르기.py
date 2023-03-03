def cutting(idx, L):
    cut = []
    cnt = 0
    for i in range(1, L+1):
        cnt += 1
        if arr[idx][i] == 1:
            cut.append(cnt)
            cnt = 0
    cut.append(cnt)
    return max(cut)


X, Y = map(int, input().split())
arr = [[0] * 101 for _ in range(2)]
N = int(input())

for i in range(N):
    d, n = map(int, input().split())
    arr[d][n] = 1

print(cutting(1, X) * cutting(0, Y))