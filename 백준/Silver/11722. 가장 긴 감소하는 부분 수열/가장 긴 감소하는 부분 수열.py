N = int(input())
arr = list(map(int, input().rstrip().split()))
lst = [arr[0]]
for i in range(N):
    if arr[i] < lst[-1]:
        lst.append(arr[i])
    else:
        for j in range(len(lst)):
            if arr[i] >= lst[j]:
                lst[j] = arr[i]
                break
print(len(lst))