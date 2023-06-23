N = int(input())
people = [tuple(map(int, input().split())) for _ in range(N)]
rlt_dict = {i: 1 for i in range(1, N+1)}

for p in range(N):
    for op in range(N):
        if people[p][0] < people[op][0] and people[p][1] < people[op][1]:
            rlt_dict[p+1] += 1
            
print(*rlt_dict.values())