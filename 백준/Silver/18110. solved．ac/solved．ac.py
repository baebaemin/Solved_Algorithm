def myRound(n):
    if 1 - (n % 1) <= 0.5:
        return int(n // 1 + 1)
    else:
        return int(n // 1)
    
    
N = int(input())
ex = myRound(N * 0.15)
people = N - (ex * 2)
scores = sorted([int(input()) for _ in range(N)])
try:
    print(myRound(sum(scores[ex:N-ex]) / people))
except:
    print(0)