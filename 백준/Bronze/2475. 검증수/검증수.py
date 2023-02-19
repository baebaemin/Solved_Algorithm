total = 0
for i in map(int, input().split()):
    total += i ** 2
print(total % 10)