N = int(input())
origin_lst = list(map(int, input().split()))
lst = sorted(list(set(origin_lst)))
n_dict = {}

for i, n in enumerate(lst):
    n_dict[n] = i

for num in origin_lst:
    print(n_dict[num], end=' ')