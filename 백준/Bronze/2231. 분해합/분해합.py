data = input()
N = int(data) #216
N_lst = list(int(n) for n in data)

min_num = N - (N_lst[0] + (len(N_lst) - 1) * 9)

while min_num < N:
    min_lst = list(int(n) for n in str(min_num))
    if N != min_num + sum(min_lst):
        min_num += 1
    else:
        print(''.join(str(ch) for ch in min_lst))
        break
else:
    print(0)