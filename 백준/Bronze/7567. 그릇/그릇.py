dish = 'I' + input()

total = 0
for i in range(len(dish)-1):
    if dish[i] != dish[i+1]:
        total += 10
    else:
        total += 5
print(total)