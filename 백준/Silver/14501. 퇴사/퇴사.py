def appointment(n, sm):
    global maxV
    if n > N:
        maxV = max(sm, maxV)
        return
    if lst[n][0]:
        appointment(n + lst[n][0], sm + lst[n][1])
    appointment(n + 1, sm)

N = int(input())
lst = [(1, 0)] + [(0, 0)] * N
for i in range(1, N+1):
    day, fee = map(int, input().split())
    if i + day <= N + 1:
        lst[i] = (day, fee)
# print(lst)
maxV = 0
appointment(0, 0)
print(maxV)