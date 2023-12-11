import sys
N, M = map(int, sys.stdin.readline().split())

never_heard = set()
for _ in range(N):
    never_heard.add(sys.stdin.readline().strip())

never_seen = set()
for _ in range(M):
    never_seen.add(sys.stdin.readline().strip())

result = sorted(list(never_heard & never_seen))
print(len(result))
print(*result, end='\n')