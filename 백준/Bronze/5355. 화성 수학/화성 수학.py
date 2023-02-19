for _ in range(int(input())):
    lst = list(input().split())
    num = float(lst[0])

    for i in lst[1:]:
        if i == '@':
            num *= 3
        elif i == '%':
            num += 5
        else:
            num -= 7
    print("{:.2f}".format(num))