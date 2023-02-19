word = input()
for i in range(len(word) // 2 + len(word) % 2):
    if word[i] != word[-1 - i]:
        print(0)
        break
else:
    print(1)