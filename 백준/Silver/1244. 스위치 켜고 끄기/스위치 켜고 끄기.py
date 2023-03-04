N = int(input())
lst = [-1] + list(map(int, input().split()))

for _ in range(int(input())):
    i = j = 1
    G, S = map(int, input().split())
    if G == 1:  # male
        while S*i <= N:
            lst[S*i] = 0 if lst[S*i] else 1
            i += 1
    else:
        lst[S] = 0 if lst[S] else 1
        while lst[S-j] != -1 and S+j <= N:
            if lst[S-j] != lst[S+j]:
                break
            else:
                lst[S-j] = 0 if lst[S-j] else 1
                lst[S+j] = 0 if lst[S+j] else 1
            j += 1

lst.pop(0)
for i in range(0, len(lst), 20):
    print(*lst[i:i + 20])