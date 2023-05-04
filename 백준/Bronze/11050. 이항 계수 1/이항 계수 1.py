import itertools
N, K = map(int, input().split())
print(len(list(itertools.combinations(range(N), K))))