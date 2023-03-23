A, B = input().split()
A_idx = B_idx = 0

for ch in A:
    if ch in B:
        A_idx = A.index(ch)
        B_idx = B.index(ch)
        break

arr = [['.'] * len(B) for _ in range(len(A))]
arr[A_idx] = B
t_arr = list(map(list, zip(*arr)))
t_arr[B_idx] = A

for j in range(len(B)):
    print(''.join(t_arr[j]))

