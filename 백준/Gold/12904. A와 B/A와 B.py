from collections import deque

def check(S, T):  # S = AB / T = ABB
    for _ in range(len(T) - len(S)):  # 3 - 2 = 1, 1번 반복할것임 2
        while Q:
            T = Q.popleft()
            if T == S:
                print(1)
                return
            if len(T) == 1:
                print(0)
                return
            if T[-1] == 'A':
                T = T[:-1]
                if T == S:
                    print(1)
                    return
                Q.append(T)
            elif T[-1] == 'B':
                T = T[:-1]
                T = T[::-1]
                if T == S:
                    print(1)
                    return
                Q.append(T)
    print(0)
    return


A = input()  # AB (2)
B = input()  # ABB (3)
Q = deque([B])  # Q에는 ABB
check(A, B)