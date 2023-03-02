def conti_num(A, B, list):
    global maxV
    if B < 0:
        if len(list)-1 > maxV:
            maxV = len(list)-1
        Q.append([len(list)-1, list[:-1]])
        return
    conti_num(B, A-B, list + [A-B])

N = int(input())
num_list = [i for i in range(N+1)]
maxV = -1
Q = []
for num in num_list:
    if 0 < num <= N:
        conti_num(N, num, [N, num])

for i in range(len(num_list)):
    if Q[i][0] == maxV:
        print(maxV)
        print(*Q[i][1])
        break