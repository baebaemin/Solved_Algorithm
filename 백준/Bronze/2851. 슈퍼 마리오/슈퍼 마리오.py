mushrooms = [int(input()) for _ in range(10)]
nyam = 0

for mushroom in mushrooms:
    nyam += mushroom
    if nyam >= 100:
        if abs(100 - nyam) > abs(100 - (nyam - mushroom)):
            nyam -= mushroom
        break
print(nyam)