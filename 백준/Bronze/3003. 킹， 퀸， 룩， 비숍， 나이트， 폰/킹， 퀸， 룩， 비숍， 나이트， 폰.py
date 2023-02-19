chess_lst = [1, 1, 2, 2, 2, 8]
crt_lst = list(map(int, input().split()))
rlt = [0] * 6

print(*[chess_lst[i] - crt_lst[i] for i in range(6)])