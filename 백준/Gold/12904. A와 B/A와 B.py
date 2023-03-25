def check(S, T):
    while Q:
        T = Q.pop(0)
        if T == S:
            return 1
        if len(T) == len(S):
            return 0
        if T[-1] == 'A':
            T = T[:-1]
            if T == S:
                return 1
            Q.append(T)
        else:
            T = T[:-1][::-1]
            if T == S:
                return 1
            Q.append(T)

s = input()
t = input()
Q = [t]
print(check(s, t))