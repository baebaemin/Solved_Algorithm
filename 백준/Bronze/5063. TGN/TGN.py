for tc in range(int(input())):
    r, e, c = map(int, input().split())
    if e - c == r:
        print('does not matter')
    elif e - c < r:
        print('do not advertise')
    else:
        print('advertise')