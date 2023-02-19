six = 6
my_place = cnt = 1
cnt = 1
goal = int(input())

while my_place < goal:
    my_place += six * cnt
    cnt += 1
print(cnt)