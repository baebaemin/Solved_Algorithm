N, r, c = map(int, input().split())
sm = 0

while N:
    area = 0
    half = 2 ** (N - 1)
    if r < half and c < half:       # 0분면
        area = 0
    elif r < half and c >= half:    # 1분면
        area = 1
        c -= half
    elif r >= half and c < half:    # 2분면
        area = 2
        r -= half
    else:                           # 3분면
        area = 3
        r -= half
        c -= half

    sm += half * half * area
    N -= 1

print(sm)