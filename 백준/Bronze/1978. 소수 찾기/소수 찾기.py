N = int(input())
arr = list(map(int, input().split()))
cnt = 0
for num in arr:
    if num == 2 or num == 3:
        cnt += 1
        continue
    if num <= 1 or not num % 2:  # 소수가 아님
        continue
    divider = 3
    while divider <= num // 2 :
        if not num % divider:   # 소수가 아님
            break
        divider += 2
    else:
        cnt += 1
print(cnt)