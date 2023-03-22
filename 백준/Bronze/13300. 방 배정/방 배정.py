N, K = map(int, input().split())
room = {0:{}, 1:{}}
for i in range(N):
    g, c = map(int, input().split())
    try:
        room[g][c] += 1
    except:
        room[g][c] = 1
        
cnt = 0
for i in range(1,7):
    try:
        cnt += room[0][i] // K + room[0][i] % K
    except: pass
    try:
        cnt += room[1][i] // K + room[1][i] % K
    except: pass

print(cnt)