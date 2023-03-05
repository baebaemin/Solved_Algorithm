N = int(input())
rlt = [i + (N - 5 * i) // 3 for i in range(N//5, -1, -1) if (N-5*i) % 3 == 0]
print(rlt[0] if rlt else -1)