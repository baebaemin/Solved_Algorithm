def game(x, y, bing, diag1, diag2):
    arr[x][y] = 0
    if not sum(arr[x]):
        bing += 1
    if not sum([arr[r][y] for r in range(5)]):
        bing += 1
    if diag1 and not sum([arr[i][i] for i in range(5)]):
        bing += 1; diag1 = 0
    if diag2 and not sum([arr[j][-j-1] for j in range(5)]):
        bing += 1; diag2 = 0
    if bing >= 3:
        return
    else: game(*bingo[numbers.pop(0)], bing, diag1, diag2)

bingo = {}
for i in range(1, 26):
    bingo[i] = (0,0)
arr = [[0] * 5 for _ in range(5)]

for i in range(5):
    c = 0
    for j in list(map(int, input().split())):
        arr[i][c] = j
        bingo[j] = (i, c)
        c += 1

numbers = []
for _ in range(5):
    for n in list(map(int, input().split())):
        numbers.append(n)
game(*bingo[numbers.pop(0)], 0, 1, 1)
print(25 - len(numbers))