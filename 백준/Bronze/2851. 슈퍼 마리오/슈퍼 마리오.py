mushrooms = [int(input()) for _ in range(10)]
nyam = 0

for mushroom in mushrooms:
    nyam += mushroom
    if nyam > 100:
        if nyam-100 > 100 - (nyam-mushroom):
            nyam -= mushroom
        break

print(nyam)
