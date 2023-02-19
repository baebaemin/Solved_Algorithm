A, B, C = 300, 60, 10
T = int(input())

if T // A >= 0:
    a = T // A
    T -= (A * a)
    if T // B >= 0:
        b = T // B
        T -= (B * b)
        if T // C >= 0:
            c = T // C
            T -= (C * c)
            if T == 0:
                print(a, b, c)
            else:
                print(-1)