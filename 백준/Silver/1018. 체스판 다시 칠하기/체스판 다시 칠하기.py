def Painting(r, c, Color1, Color2):
    global cnt
    global minV
    cnt = 0
    for adjR in range(8):
        for adjC in range(4):
            newR, newC = r + adjR, c + adjC*2
            if not newR % 2:                      # 짝수행일떄
                if arr[newR][newC] != Color1:     # 짝수열일때
                    cnt += 1
                if arr[newR][newC+1] != Color2:   # 홀수열일때
                    cnt += 1
            else:
                if arr[newR][newC] != Color2:   # 홀수행일때
                    cnt += 1
                if arr[newR][newC+1] != Color1:
                    cnt += 1
            if cnt > minV:
                break
    else:
        minV = min(minV, cnt)

R, C = map(int, input().split())
arr = [input() for _ in range(R)]
minV = 0x99999
for startR in range(R - 8 + 1):
    for startC in range(C - 8 + 1):
        Painting(startR, startC, 'B', 'W')  # B로 시작하는 체스판
        Painting(startR, startC, 'W', 'B')  # W로 시작하는 체스판

print(minV)