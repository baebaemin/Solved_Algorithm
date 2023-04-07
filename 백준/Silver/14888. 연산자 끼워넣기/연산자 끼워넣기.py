import itertools

N = int(input())
nums = list(map(int, input().split()))
calcs = list(map(int, input().split()))
maxV = -11 ** 10
minV = -maxV

calc_lst = []
for i in range(4):
    if calcs[i]:
        for j in range(calcs[i]):
            calc_lst.append(i+1)
C = len(calc_lst)
nPr = list(set(itertools.permutations(calc_lst, C)))
for line in nPr:
    temp = nums[0]
    for n in range(C):
        if line[n] == 1: 
            temp += nums[n+1]
        elif line[n] == 2:
            temp -= nums[n+1]
        elif line[n] == 3:
            temp *= nums[n+1]
        else:
            if temp >= 0:
                temp //= nums[n+1]
            else:
                temp = (-temp // nums[n+1]) * -1
    maxV = max(temp, maxV)
    minV = min(temp, minV)

print(maxV)
print(minV)