played = list(map(int, input().split()))
asc = list(range(1, 9))

if played == asc:
    print('ascending')
elif played == asc[::-1]:
    print('descending')
else:
    print('mixed')