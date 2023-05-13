import sys; input = sys.stdin.readline

N = int(input())
arr = set(map(int, input().split()))
M = int(input())
listM = list(map(int, input().split()))
for m in listM:
    if m in arr: print(1)
    else: print(0)