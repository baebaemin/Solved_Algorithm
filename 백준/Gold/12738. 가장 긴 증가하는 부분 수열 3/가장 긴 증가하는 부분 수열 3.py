import bisect

N = int(input())
arr = list(map(int, input().rstrip().split()))
lst = [arr[0]]

for i in range(N):
    if arr[i] > lst[-1]:
        lst.append(arr[i])
    else:
        id = bisect.bisect_left(lst, arr[i])
        lst[id] = arr[i]
        
print(len(lst))