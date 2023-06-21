N = int(input())
rlt = 1

for i in range(1, N+1):
    rlt *= i

rlt = str(rlt)
cnt = 0
for r in range(len(rlt)-1, -1, -1):
    if rlt[r] == '0':
        cnt += 1
    else:
        break
print(cnt)