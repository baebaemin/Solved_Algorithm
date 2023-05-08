import sys; input = sys.stdin.readline
N = int(input())
arr = [(0, 0) for _ in range(N)]

for i in range(N):
    arr[i] = tuple(map(int, input().split()))
new_arr = sorted(arr, key = lambda x : (x[0], x[1]))

for j in range(N):
    print(*new_arr[j])