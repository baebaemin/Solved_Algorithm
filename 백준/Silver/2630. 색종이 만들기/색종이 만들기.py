N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
white, blue = 0, 0

def cutting(sr, sc, N):
    global white, blue
    # 들어온 구역의 모든 원소를 합해보기
    section_sum = sum(sum(arr[i][sc:sc+N]) for i in range(sr, sr+N))

    # 종료조건
    if not section_sum:
        white += 1
        return
    elif section_sum == N ** 2:
        blue += 1
        return

    # 더 쪼개야 할 때
    else:
        cutting(sr, sc, N//2)
        cutting(sr, sc+N//2, N//2)
        cutting(sr+N//2, sc, N//2)
        cutting(sr+N//2, sc+N//2, N//2)


cutting(0, 0, N)
print(white)
print(blue)
