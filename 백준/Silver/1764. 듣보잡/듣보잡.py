import sys
N, M = map(int, sys.stdin.readline().split())

person_dict = {}
person_lst = []

for _ in range(N):
    name = sys.stdin.readline().strip()
    person_dict[name] = 0

for _ in range(M):
    name = sys.stdin.readline().strip()
    try:
        person_dict[name] += 1
        person_lst.append(name)
    except:
        pass

print(len(person_lst))
person_lst.sort()
print(*person_lst, sep='\n')