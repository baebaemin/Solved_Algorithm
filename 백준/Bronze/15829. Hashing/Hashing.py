L = int(input())
line = input()
ans = i = 0
for i in range(L):
    ans += (ord(line[i]) - 96) * (31 ** i)
print(ans)