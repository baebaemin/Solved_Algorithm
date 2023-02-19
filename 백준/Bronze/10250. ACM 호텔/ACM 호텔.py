import sys

T = int(sys.stdin.readline())

for test_case in range(T):
    H, W, N = map(int, input().split())
    lst = []

    for nth in range(1, W + 1):
        for floor in range(1, H + 1):
            if len(lst) < N:
                lst.append((floor, nth))
            else:
                break

    print(('% 2d' % lst[-1][0] + '%02d' % lst[-1][1]).lstrip())