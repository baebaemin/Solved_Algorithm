from itertools import product
target = int(input())
broken_N = int(input())
minV = abs(target - 100)        # 채널 100에서 시작
if broken_N:
    broken_lst = list(map(int, input().split()))
    my_btn_lst = [str(i) for i in range(10) if i not in broken_lst]
    if minV:
        for i in range(1, 7):   # 6자리 숫자까지
            for comb in product(my_btn_lst, repeat=i):
                n = int(''.join(comb))
                cnt = i + abs(n - target)
                minV = min(minV, cnt)
    print(minV)
else:                           # 고장난 버튼이 없을 때
    ans = min(minV, len(str(target)))
    print(ans)
