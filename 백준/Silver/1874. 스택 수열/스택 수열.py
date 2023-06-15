import sys
input = sys.stdin.readline

N = int(input())
line = [int(input()) for _ in range(N)]

t = 0
stack = [0]
ans = []
for i in range(1, N+1):
    if i <= line[t]:
        ans.append('+')
        stack.append(i)
    while stack[-1] == line[t]:
        ans.append('-')
        stack.pop()
        t += 1
        if t >= N:
            break
    if not stack or stack != [0] and t >= N:
        print('NO')
        break
else:
    if stack == [0]:
        for a in ans:
            print(a)
    else:
        print('NO')