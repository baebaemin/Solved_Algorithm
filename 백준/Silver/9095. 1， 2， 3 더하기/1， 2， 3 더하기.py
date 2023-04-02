def plus(sm):
    global cnt
    if sm >= goal:
        if sm == goal: cnt += 1
        return
    plus(sm+1); plus(sm + 2); plus(sm+3)

for _ in range(int(input())):
    goal = int(input())
    cnt = 0
    plus(0)
    print(cnt)