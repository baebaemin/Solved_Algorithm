T = int(input())
for tc in range(1, T+1):
    A, B = map(int, input().split())
    if A > B:
        A, B = B, A

    lst = []
    while A != 0:
        lst.append(A)
        A //= 2

    while B != 0:
        B //= 2
        if B in lst:
            print(B * 10)
            break