N = int(input())
arr = list(map(int, input().rstrip().split()))
lst = arr[:]

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            lst[i] = max(lst[i], lst[j] + arr[i])

print(max(lst))