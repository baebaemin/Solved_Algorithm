N = int(input())
arr = [[] for _ in range(N)]

for i in range(N):
    word = input()
    arr[i] = (len(word), word)

sortedArr = sorted(set(arr))
for j in range(len(sortedArr)):
    print(sortedArr[j][1])