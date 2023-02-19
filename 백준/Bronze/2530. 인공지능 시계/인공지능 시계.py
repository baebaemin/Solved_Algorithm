H, M, S = map(int, input().split())
cook = int(input())

S += cook
if S > 59:
    M += S // 60
    S -= 60 * (S // 60)
    if M > 59:
        H += M // 60
        M -= 60 * (M // 60)
        if H > 23:
            H -= 24 * (H // 24)

print(H, M, S)