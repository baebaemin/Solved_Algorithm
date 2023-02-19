N = int(input())

k = 2
while N != 1:
    if N % k == 0:
        N //= k
        print(k)
    else:
        k += 1
    if N == 1:
        break