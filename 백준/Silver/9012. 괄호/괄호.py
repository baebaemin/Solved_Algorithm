from collections import deque

for _ in range(int(input())):
    line = input()
    Q = deque()
    for ch in line:
        if ch == '(': 
            Q.append(ch)
        else:
            try: Q.pop()
            except: print('NO'); break
    else:
        if Q: print('NO')
        else: print('YES')