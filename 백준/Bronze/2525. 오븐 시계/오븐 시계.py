H, M = map(int, input().split())
cook = int(input())

M += cook
if M > 59:
    H += M // 60
    M -= 60 * (M // 60)
    if H > 23:
        H -= 24 * (H // 24)

print(H, M)