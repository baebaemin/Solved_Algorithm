lines = list(map(str, input().split('-')))
sm = sum(map(int, lines[0].split('+')))
minus = 0
for line in lines[1:]:
    minus += sum(map(int, line.split('+')))
print(sm-minus)