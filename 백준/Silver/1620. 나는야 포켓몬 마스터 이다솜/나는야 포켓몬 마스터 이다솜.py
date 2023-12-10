import sys

N, M = map(int, sys.stdin.readline().split())
poke_lst = ['' for _ in range(N+1)]
poke_dict = {}

for i in range(1, N+1):
    data = sys.stdin.readline().strip()
    poke_lst[i] = data
    poke_dict[data] = i

for j in range(M):
    question = sys.stdin.readline().strip()
    if question.isdigit():
        print(poke_lst[int(question)])
    else:
        print(poke_dict[question])