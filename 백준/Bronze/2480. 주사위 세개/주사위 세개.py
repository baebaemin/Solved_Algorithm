a, b, c = map(int, input().split())
three = {a, b, c}
lst = [a, b, c]

if len(three) == 1:
    print(10000 + a * 1000)
elif len(three) == 3:
    print(max(lst) * 100)
else:
    if max(lst) == sorted(lst)[1]:
        print(1000 + max(lst) * 100)
    else:
        print(1000 + min(lst) * 100)