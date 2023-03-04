W, H = map(int, input().split())
x, y = map(int, input().split())
t = int(input())
sumX, sumY = x+t, y+t

if sumX // W % 2 == 0: print(sumX % W, end=' ')
else: print(W - (sumX % W), end=' ')

if sumY // H % 2 == 0: print(sumY % H)
else: print(H - (sumY % H))