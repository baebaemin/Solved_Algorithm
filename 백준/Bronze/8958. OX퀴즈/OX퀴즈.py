T = int(input())
for tc in range(T):
    total = 0
    cnt = 1
    for ch in input():
        if ch == 'O':
            total += cnt
            cnt += 1
        else:
            cnt = 1
    print(total)