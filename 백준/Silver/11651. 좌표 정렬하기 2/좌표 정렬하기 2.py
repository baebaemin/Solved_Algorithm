N = int(input())
lst = [[] for _ in range(N)]

for i in range(N):
    lst[i] = list(map(int, input().split()))

lst = sorted(lst, key=lambda x : (x[1], x[0]))

for l in lst:
    print(*l)
