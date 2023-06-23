for _ in range(int(input())):
    M, N, x, y = map(int, input().split())
    year = i = 0
    while True:
        year = i * M + x
        if year > N * M:
            print(-1)
            break
        elif not year % N and y == N or year % N == y:
            print(year)
            break
        i += 1