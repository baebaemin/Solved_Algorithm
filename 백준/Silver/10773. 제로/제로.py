N = int(input())
z = []
for i in range(N):
    num = int(input())
    if num == 0:
        z.pop()
    else:
        z.append(num)
print(sum(z))