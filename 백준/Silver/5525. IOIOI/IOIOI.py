import re
N = int(input())
L = int(input())
pattern = 'OI'
string = input()
idx_lst = [i.start() for i in re.finditer(pattern, string)]  # [1, 3, 5, 7, 10]
if not idx_lst[0]:
    idx_lst = idx_lst[1:]
cnt = i = 0

while i < len(idx_lst):  # len(idx_lst) = 5
    if string[idx_lst[i]-((N-1)*2+1):idx_lst[i]] == 'I' + 'OI' * (N-1):
        cnt += 1
        while i < len(idx_lst)-1:   # i = 0, 1, 2, 3 // 지금 i는 0
            if idx_lst[i+1] - idx_lst[i] == 2:  # i가 3일때 틀리
                cnt += 1
                i += 1
            else:  # 찾다가...
                i += 1
                break
        else: i += 1
    else: i += 1

print(cnt)
