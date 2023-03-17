N = int(input())
seats = input()

cnt_S = seats.count('S')
cnt_L = seats.count('LL')
if cnt_L == 0:
    cnt_L = -1

print(cnt_S + cnt_L + 1)