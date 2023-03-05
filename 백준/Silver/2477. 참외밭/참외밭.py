N = int(input())
d_lst = [0] * 6
lst = [0] * 6

for i in range(6):
    d_lst[i], lst[i] = tuple(map(int, input().split()))
for j in range(6):
    if d_lst[j % 6] == d_lst[(j+2) % 6] and d_lst[(j+1) % 6] == d_lst[(j+3) % 6]:
        break

print(N * (lst[(j-1)%6] * lst[(j-2)%6] - (lst[(j+1)%6] * lst[(j+2)%6])))