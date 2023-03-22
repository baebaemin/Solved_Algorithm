N, K = map(int, input().split())
room = {0:{}, 1:{}}
for i in range(N):
    g, c = map(int, input().split())
    try:
        room[g][c] += 1
    except:
        room[g][c] = 1

cnt = 0
for j in range(1, 7):
    if j in room[0]:
        cnt += room[0][j] // K + room[0][j] % K
    if j in room[1]:
        cnt += room[1][j] // K + room[1][j] % K
print(cnt)