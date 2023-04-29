N = int(input())
lst = [[] for _ in range(201)]
for i in range(N):
    age, name = map(str, input().split())
    lst[int(age)].append(name)

for j in range(1, 201):
    if lst[j]:
        for k in range(len(lst[j])):
            print(j, lst[j][k])