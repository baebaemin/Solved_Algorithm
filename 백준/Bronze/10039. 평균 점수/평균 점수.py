lst = []
for _ in range(5):
    n = int(input())
    if n < 40:
        n = 40
    lst.append(n)
print(round(sum(lst) / 5))