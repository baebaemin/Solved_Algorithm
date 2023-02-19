while 1:
    div_lst = [1]
    n = int(input())
    if n == -1:
        break
    i = 2

    # 약수
    while i <= n // 2:
        if n % i == 0:
            div_lst.append(i)
        i += 1
    div_lst.append(n)

    if sum(div_lst) - n == n:
        print(n, '=', end=' ')
        rev = sorted(div_lst)
        print(*rev[:-1], sep=' + ')
    else:
        print(n, 'is NOT perfect.')