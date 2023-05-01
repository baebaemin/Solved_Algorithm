arr = [[1] + [0] * 14 for _ in range(15)]

for i in range(15):
    arr[0][i] = i+1

for fl in range(1, 15): # 1부터 13까지
    for room in range(15): # 0부터 13까지 (1~14호)
        arr[fl][room] = sum(arr[fl-1][:room+1])

for _ in range(int(input())):
    K = int(input())
    N = int(input())
    print(arr[K][N-1])
